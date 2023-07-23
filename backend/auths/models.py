from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.contrib.auth.validators import UnicodeUsernameValidator

from guardian.mixins import GuardianUserMixin

from lavish.mixins import (
    AbstractModel
)

from .managers import UserManager


class User(
    AbstractModel, AbstractBaseUser, PermissionsMixin, GuardianUserMixin
):
    """
    User model overwritten for extendability
    Make sure to refer to the User model with settings.AUTH_USER_MODEL

    Richard, 23.05.2023
    """
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=255,
        null=True,
        unique=True,
        help_text=_("Required, Please enter your Email Address."),
        error_messages={
            'unique': _("This email already exists."),
        },
    )
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=255,
        null=True,
        unique=True,
        help_text=_(
            "Required. 256 characters or fewer. "
            "Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=128, blank=True
    )
    middle_name = models.CharField(
        verbose_name=_("Middle name"), max_length=128, blank=True
    )
    last_name = models.CharField(
        verbose_name=_("Last name"), max_length=128, blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Date joined"), default=timezone.now
    )

    force_change_password = models.BooleanField(
        verbose_name=_("Force change password"),
        default=False,
        help_text=_(
            "Force user to change password"
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @cached_property
    def id(self):
        """
        Retrieve uuid from user (some 3rd party library still using user.id)
        """
        return self.pk

    @property
    def is_banned(self):
        if self.is_active:
            return False
        return True

    class Meta:
        ordering = ('-created_at', )
