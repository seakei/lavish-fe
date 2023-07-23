from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from treebeard.mp_tree import MP_Node

from lavish.mixins import (
    AbstractModel
)

from .managers import (
    BusinessPartnerManager,
)
from .const import (
    PERSON,
    CATEGORY_CHOICES,
    PROFILE_STATUS_CHOICES,
    NEW,
    ROLE_CHOICES,
    CUSTOMER,
    BRANCH_CHOICES
)

UserModel = get_user_model()


class BusinessPartner(AbstractModel):
    """
    Model to store BusinessPartner information.

    Richard, 23.05.2023
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name='partner',
        on_delete=models.CASCADE
    )

    category = models.PositiveSmallIntegerField(
        verbose_name=_("Category"),
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        default=PERSON,
        help_text=_("Choose from the list.")
    )

    profile_status = models.PositiveSmallIntegerField(
        verbose_name=_("Profile Status"),
        null=True,
        blank=True,
        choices=PROFILE_STATUS_CHOICES,
        default=NEW,
        help_text=_("Required, Choose from the list")
    )

    name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=255,
        blank=True,
        default='',
        help_text=_("Required, Maximum of 255 Characters."),
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=255,
        null=True,
        help_text=_("Please enter your Email Address."),
    )

    ic_number = models.CharField(
        verbose_name=_("IC Number"),
        max_length=40,
        blank=True,
        default='',
        help_text=_("Maximum of 40 digits")
    )

    passport_number = models.CharField(
        verbose_name=_("Passport Number"),
        max_length=40,
        blank=True,
        default='',
        help_text=_("Maximum of 40 digits")
    )

    phone_number = models.CharField(
        verbose_name=_("Phone Number"),
        max_length=40,
        blank=True,
        default='',
        help_text=_("Maximum of 40 digits")
    )

    customer_from = models.CharField(
        verbose_name=_("Customer From"),
        max_length=100,
        blank=True,
        default='',
        help_text=_("Source of Customer")
    )

    address = models.TextField(
        verbose_name=_("Address"),
        blank=True,
        default='',
        help_text=_(
            "Optional, Add any extra notes related to the Loan."
        )
    )

    language = models.CharField(
        verbose_name=_("Language"),
        max_length=100,
        blank=True,
        default='',
        help_text=_("Please select your language")
    )

    role = models.PositiveSmallIntegerField(
        verbose_name=_("User Role"),
        null=True,
        blank=True,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
        help_text=_("Required, Choose from the list")
    )

    number = models.CharField(
        verbose_name=_("Number"),
        max_length=25,
        blank=True,
        default='',
    )

    branch = models.PositiveSmallIntegerField(
        verbose_name=_("Branch"),
        null=True,
        blank=True,
        choices=BRANCH_CHOICES,
        default=None,
        help_text=_("Choose from the list")
    )

    objects = BusinessPartnerManager()

    class Meta:
        verbose_name = _("Business Partner")
        verbose_name_plural = _("Business Partners")

    SYSTEM_USER_FIELDS = ('phone_number', )

    def __str__(self):
        return f"{self.pk}"

    def get_absolute_url(self):
        return reverse(
            'partners:partner-detail',
            kwargs={'pk': self.pk}
        )


class Hierarchy(AbstractModel, MP_Node):
    partner = models.OneToOneField(
        'BusinessPartner',
        related_name='hierarchy',
        on_delete=models.CASCADE
    )
