from django.contrib.auth import get_user_model

from partners.const import CUSTOMER
from partners.models import BusinessPartner

UserModel = get_user_model()


def create_or_update_partner_models_from_user(user, is_update=False, **kwargs):
    partner_attrs = kwargs.get('partner', {})

    if not is_update:
        partner, is_created = BusinessPartner.objects.get_or_create(
            user=user, role=partner_attrs.get('role', CUSTOMER)
        )
    else:
        partner = BusinessPartner.objects.get(user=user)

    partner.refresh_from_db()

    name = f'{user.first_name} {user.last_name}'
    partner.name = name
    partner.email = user.email

    for k, v in partner_attrs.items():
        setattr(partner, k, v)

    partner.save()
