from django.db import models
from django.db.models import F
from django.utils.translation import ugettext_lazy as _

from lavish.mixins import (
    AbstractModel
)


class Numbering(AbstractModel):
    """
    Simple numbering model

    Richard, 17.06.2023
    """
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=100,
        unique=True
    )
    running_number = models.PositiveIntegerField(
        verbose_name=_("Running Number"),
        null=True,
        default=0,
        help_text=_("The current running number")
    )

    class Meta:
        verbose_name = _("Numbering")
        verbose_name_plural = _("Numberings")

    def __str__(self):
        return f"{self.category}: {self.running_number}"

    def generate_running_number(self):
        """
        Generate a number
        """
        self.running_number = F('running_number') + 1
        self.save()
        self.refresh_from_db()
        return self.running_number
