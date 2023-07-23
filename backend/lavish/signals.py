from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver


from numberings.models import Numbering
from partners.models import BusinessPartner
from partners.const import CUSTOMER
from vehicles.models import Vehicle, Booking
from salesorders.models import SalesOrder
from inspections.models import Inspection


@receiver(post_save, sender=BusinessPartner)
@receiver(post_save, sender=Booking)
@receiver(post_save, sender=Vehicle)
@receiver(post_save, sender=SalesOrder)
@receiver(post_save, sender=Inspection)
def assign_numberin(sender, instance, created, **kwargs):
    """
    Assign Numbering

    Richard, 17.06.2023
    """
    ct = ContentType.objects.get_for_model(instance)

    if created:
        prefix_mapping = {
            'vehicle': 'CAR',
            'booking': 'BKK',
            'salesorder': 'SAL',
            'inspection': 'INS'
        }
        if ct.model == 'businesspartner':
            if instance.role == CUSTOMER:
                category = f'{ct.model.upper()}_CUSTOMER'
                prefix = 'CST'
            else:
                category = f'{ct.model.upper()}_SYSTEMUSER'
                prefix = 'USR'
        else:
            category = f'{ct.model.upper()}'
            prefix = prefix_mapping.get(f'{ct.model}')

        numbering, created = Numbering.objects.select_for_update().get_or_create(
            category=category
        )

        _runnning_number = numbering.generate_running_number()
        type(instance).objects.filter(pk=instance.pk).update(number=f'{prefix}{_runnning_number:06}')
