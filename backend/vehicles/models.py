from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from lavish.mixins import (
    AbstractModel,
)

from .managers import BookingManager

from .const import BOOKING_TYPE
from partners.const import BRANCH_CHOICES

from partners.models import BusinessPartner

UserModel = get_user_model()


class Vehicle(AbstractModel):
    """
    Model to store Car information.

    Richard, 28.05.2023
    """

    partner = models.ForeignKey(
        BusinessPartner,
        null=True,
        blank=True,
        related_name='vehicles',
        on_delete=models.CASCADE,
    )

    car_plate = models.CharField(
        verbose_name=_("Car Plate No."),
        max_length=50,
        blank=True,
        default='',
        help_text=_("Required, Maximum of 50 Characters."),
    )

    car_brand = models.CharField(
        verbose_name=_("Car Brand."),
        max_length=255,
        blank=True,
        default='',
        help_text=_("Required, Maximum of 255 Characters."),
    )

    branch = models.PositiveSmallIntegerField(
        verbose_name=_("Branch"),
        null=True,
        blank=True,
        choices=BRANCH_CHOICES,
        default=None,
        help_text=_("Choose from the list"),
    )

    package = models.CharField(
        verbose_name=_("Car Plate No."),
        max_length=150,
        blank=True,
        default='',
        help_text=_("Required, Maximum of 150 Characters."),
    )

    remarks = models.TextField(
        verbose_name=_("Remarks"),
        blank=True,
        default='',
        help_text=_("Optional, Add any extra notes related to the Loan."),
    )

    number = models.CharField(
        verbose_name=_("Number"),
        max_length=25,
        blank=True,
        default='',
    )

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.pk}"


class Booking(AbstractModel):
    """
    Model to store Booking information.

    Richard, 01.06.2023
    """

    vehicle = models.ForeignKey(
        'Vehicle',
        related_name='bookings',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    booking_date = models.DateTimeField(
        verbose_name=_("Booking Date"),
        null=True,
        blank=True,
        help_text=_("Optional, time when customer do the appointment"),
    )

    follow_up_date = models.DateTimeField(
        verbose_name=_("Booking Date"),
        null=True,
        blank=True,
        help_text=_("Optional, time when customer do the follow up"),
    )

    booking_duration = models.DecimalField(
        verbose_name=_("Booking Duration"),
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
    )

    booking_type = models.PositiveSmallIntegerField(
        verbose_name=_("Booking Type"),
        choices=BOOKING_TYPE,
        null=True,
        blank=True,
    )

    remark = models.CharField(
        verbose_name=_("Remark"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Optional"),
    )

    number = models.CharField(
        verbose_name=_("Number"),
        max_length=25,
        blank=True,
        default='',
    )

    objects = BookingManager()

    class Meta:
        ordering = ('booking_date',)
