from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from partners.models import BusinessPartner
from vehicles.models import Booking

from lavish.mixins import (
    AbstractModel
)

from .managers import (
    SalesOrderManager,
    OrderManager,
    ItemManager,
    SignatureManager,
)

from .const import (
    CUST_REQUIREMENT,
    EASY,
    JOB_TYPE,
    PRODUCT_PACKAGE,
    ORDER_MODE,
    ITEM_NAME,
    PART_STATUS,
    # ACCESSORIES,
    SURCHARGE_VEHICLE_TYPE,
    TEAM_TYPE,
    VEHICLE_PART,
    DISCOUNT_TYPE,
    ORDER_TYPE,
)

UserModel = get_user_model()

class SalesOrder(AbstractModel):
    """
    Sales Order Model.
    """
    sales_person_in_charge = models.ForeignKey(
        BusinessPartner,
        max_length = 40,
        null = True,
        blank = True,
        related_name = 'businesspartner',
        on_delete=models.PROTECT
    )
    booking = models.ForeignKey(
        Booking,
        related_name='booking',
        verbose_name=_("Booking"),
        on_delete=models.PROTECT,
        null = True,
        blank = True,
    )
    installment_plan = models.BooleanField(
        default=False,
        null = True,
        blank = True,
    )
    cust_requirement = models.PositiveSmallIntegerField(
        verbose_name=_("Customer Requirement"),
        null=True,
        blank=True,
        choices=CUST_REQUIREMENT,
        default=EASY,
    )
    duration = models.DecimalField(
        verbose_name=_("Duration"),
        decimal_places=1,
        max_digits=5,
        blank=True,
        null=True
    ) # might remove -> moved to booking
    assigned_team = models.PositiveSmallIntegerField(
        verbose_name=_("Team"),
        choices=TEAM_TYPE,
        blank=True,
        null=True
    )
    surcharge_type = models.PositiveSmallIntegerField(
        verbose_name=_("Surcharge"),
        choices=SURCHARGE_VEHICLE_TYPE,
        null = True,
        blank = True,
    )
    surcharge_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Surcharge Price"),
        default = 0,
        null = True,
        blank = True,
    )
    upgrade_or_alacarte = models.BooleanField(
        verbose_name=_("Upgrade/ Add Ala-Carte"),
        default = False,
        null = True,
        blank = True,
    )
    remove_charge = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Remove"),
        default = 0,
        null = True,
        blank = True,
    )
    sun_visor_charge = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Sun Visor"),
        default = 0,
        null = True,
        blank = True,
    )
    discount = models.BooleanField(
        verbose_name=_("Discount"),
        default = False,
        null = True,
        blank = True,
    )
    discount_type = models.PositiveSmallIntegerField(
        verbose_name=_("Discount Type"),
        choices=DISCOUNT_TYPE,
        null = True,
        blank = True,
    )
    discount_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Discount Amount"),
        default = 0,
        null = True,
        blank = True,
    )
    cust_reference = models.BooleanField(
        verbose_name=_("Customer Reference Fee"),
        default = False,
        null = True,
        blank = True,
    )
    reference_fee = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Reference Fee"),
        default = 0,
        null = True,
        blank = True,
    )
    total_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Total"),
        default = 0,
        null = True,
        blank = True,
    )
    balance_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Balance"),
        default = 0,
        null = True,
        blank = True,
    )
    # not a FKey
    signature_id = models.CharField(
        verbose_name=_("SignatureId"),
        max_length=40,
        null = True,
        blank = True,
    )
    number = models.CharField(
        verbose_name=_("Number"),
        max_length=25,
        blank=True,
        default='',
    )
    objects = SalesOrderManager()

    class Meta:
        verbose_name = _("Sales Order")
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.pk}"

class Signature(AbstractModel):
    """
    Sales order Signature binary data Model.
    """
    signature_data = models.BinaryField(
        verbose_name=_("Signature Image Data"),
        null = True,
        blank = True,
    )
    salesorder = models.ForeignKey(
        SalesOrder,
        related_name = 'salesorder_sig',
        on_delete=models.PROTECT
    )
    objects = SignatureManager()

    class Meta:
        verbose_name = _("Signature")

    def __str__(self):
        return f"{self.pk}"

class Order(AbstractModel):
    """
    Order Model. Mutiple orders in a sales order
    """
    salesorder = models.ForeignKey(
        SalesOrder,
        related_name = 'salesorder',
        on_delete=models.PROTECT
    )
    order_type = models.PositiveSmallIntegerField(
        verbose_name=_("Order Type"),
        choices=ORDER_TYPE,
        null = True,
        blank = True,
    )
    order_mode = models.PositiveSmallIntegerField(
        verbose_name=_("Order Mode"),
        choices=ORDER_MODE,
        null = True,
        blank = True,
    )
    product_package = models.PositiveSmallIntegerField(
        verbose_name=_("Product Package"),
        choices=PRODUCT_PACKAGE,
        null = True,
        blank = True,
    )
    item_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name=_("Order Price"),
        default = 0,
        null = True,
        blank = True,
    )

    objects = OrderManager()

    class Meta:
        verbose_name = _("Order")
        ordering = ('created_at', )

    def __str__(self):
        return f"{self.pk}"


class OrderItem(AbstractModel):
    """
    OrderItem Model. Mutiple Items in an order
    """
    order = models.ForeignKey(
        Order,
        related_name = 'order',
        on_delete=models.PROTECT
    )
    vehicle_part = models.CharField(
        max_length=255,
        verbose_name=_("Part"),
        null=True,
        blank=True,
    )
    # vehicle_part = models.PositiveSmallIntegerField(
    #     verbose_name=_("Part"),
    #     choices=VEHICLE_PART,
    #     null=True,
    #     blank=True,
    # )
    claim_insurance = models.BooleanField(
        verbose_name=_("Claim Under Insurance"),
        default=False,
        null=True,
        blank=True,
    )
    job_type = models.CharField(
        max_length=100,
        verbose_name=_("Job"),
        choices=JOB_TYPE,
        null=True,
        blank=True,
    )
    item_name = models.CharField(
        max_length=255,
        verbose_name=_("Item Name"),
        null=True,
        blank=True,
    ) 
    # item_name = models.PositiveSmallIntegerField(
    #     verbose_name=_("Item Name"),
    #     choices=ITEM_NAME,
    #     null=True,
    #     blank=True,
    # )   
    remarks = models.CharField(
        verbose_name=_("Remarks"),
        max_length=255,
        null=True,
        blank=True,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_("Gift Status"),
        choices=PART_STATUS,
        null=True,
        blank=True,
    )
    """
    to_accessories = models.PositiveSmallIntegerField(
        verbose_name=_("To Accessories"),
        choices=ACCESSORIES,
        null=True,
        blank=True,
    )
    """
    addon = models.CharField(
        max_length=255,
        verbose_name=_("Add-On"),
        null=True,
        blank=True,
    )
    # addon = models.PositiveSmallIntegerField(
    #     verbose_name=_("Add-On"),
    #     choices=ITEM_NAME,
    #     null=True,
    #     blank=True,
    # )


    objects = ItemManager()

    class Meta:
        verbose_name = _("Item")
        ordering = ('created_at', )

    def __str__(self):
        return f"{self.pk}"
