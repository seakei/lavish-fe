import uuid

from django.conf import settings
from django.forms.models import model_to_dict
from django.db import models
from django.utils.translation import gettext_lazy as _

from auths.middleware import get_current_user


class TimeStampedModelMixin(models.Model):
    """
    Abstract model which adds timestamp fields to any models

    Richard, 23.05.2023
    """
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now=False,
        auto_now_add=True,
        db_index=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        auto_now_add=False,
        db_index=True
    )

    class Meta:
        abstract = True


class AuditedModelMixin(models.Model):
    """
    Abstract model which adds foreign keys to the user model to store the
    creator or the modifier of the recored for auditing purposes

    Fields are made nullable for objects created by Shell
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Created by"),
        related_name='%(app_label)s_%(class)s_created_by',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        editable=False
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Updated by"),
        related_name='%(app_label)s_%(class)s_modified_by',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        editable=False
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Overwritting save to ensure the created_by is automatically populated
        """
        # Fallback for the self.created_by
        # Leave this import in here because it is a model level import and will
        # break the model file if you move it to the top
        from django.contrib.auth import get_user_model
        UserModel = get_user_model()
        try:
            _created_by = UserModel.objects.get(pk=self.created_by_id)
        except UserModel.DoesNotExist:
            _created_by = None
        # End of fallback

        if self._state.adding and _created_by is None:
            self.created_by = get_current_user()
        self.updated_by = get_current_user()
        super().save(*args, **kwargs)


class UUIDModelMixin(models.Model):
    """
    Abstract model which replaces the default Django primary key field with a
    proper UUID

    Richard, 23.05.2023
    """
    uuid = models.UUIDField(
        verbose_name=_("UUID Identifier"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("Required, PrimaryKey none-editable"),
        db_index=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.uuid)


class IsActiveModelMixin(models.Model):
    """
    Abstract models which add is_active field
    """
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_(
            "Designates whether this data is active or deleted"
        )
    )

    class Meta:
        abstract = True


class AbstractModel(
    AuditedModelMixin,
    UUIDModelMixin,
    TimeStampedModelMixin,
    IsActiveModelMixin,
    models.Model
):
    """
    Overwritten the Django Model to be used as a default for all Models

    Richard, 23.05.2023
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ModelDiffMixin(object):
    """
    A model mixin that tracks model fields' values and provide some useful api
    to know what fields have been changed.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        super(ModelDiffMixin, self).save(*args, **kwargs)
        self.__initial = self._dict

    @property
    def _dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])

    @property
    def _initial(self):
        return self.__initial
