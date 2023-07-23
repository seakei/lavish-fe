import os
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from salesorders.models import OrderItem

from lavish.mixins import (
    AbstractModel
)

from .managers import (
    InspectionManager,
    SignatureManager,
    InspectionUploadManager
)

UserModel = get_user_model()

class Inspection(AbstractModel):
    """
    Inspection Model.
    """
    order_item = models.ForeignKey(
        OrderItem,
        related_name='orderitem',
        verbose_name=_("Order_item"),
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )
    condition = models.BooleanField(
        verbose_name=_("Condition"),
        default=False,
        null=True,
        blank=True,
    )
    remarks = models.CharField(
        verbose_name=_("Remarks"),
        max_length=255,
        null=True,
        blank=True,
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
    objects = InspectionManager()

    class Meta:
        verbose_name = _("Inspection")
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.pk}"

class InspectionSignature(AbstractModel):
    """
    inspection Signature binary data Model.
    """
    signature_data = models.BinaryField(
        verbose_name=_("Signature Image Data"),
        null = True,
        blank = True,
    )
    inspection = models.ForeignKey(
        Inspection,
        related_name = 'inspection_sig',
        on_delete=models.CASCADE
    )
    objects = SignatureManager()

    class Meta:
        verbose_name = _("Inspection Signature")

    def __str__(self):
        return f"{self.pk}"

def get_upload_path(instance, filename):
    return os.path.join(instance.inspection.number, filename)

class InspectionUpload(AbstractModel):
    """
    inspection upload Model.
    """
    inspection = models.ForeignKey(
        Inspection,
        related_name = 'inspection',
        on_delete=models.CASCADE
    )
    upload_file = models.FileField(
        verbose_name=_("Inspection Upload file"),
        upload_to=get_upload_path,
        max_length=255,
        null = True,
        blank = True,
    )
    objects = InspectionUploadManager()

    class Meta:
        verbose_name = _("Inspection Upload")

    def __str__(self):
        return f"{self.pk}"
