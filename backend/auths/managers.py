from django.db.models import QuerySet
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserQuerySet(QuerySet):
    """
    QuerySet for Users

    Richard, 23.05.2023
    """


class UserManager(BaseUserManager):
    """
    ModelManager for Users

    Richard, 23.05.2023
    """

    def _create_user(
        self,
        email=None,
        username=None,
        password=None,
        **extra_fields
    ):
        """
        creates and saves a User with the given
        Email, Username and password.
        """
        if email:
            email = self.normalize_email(email)

        if username:
            username = self.model.normalize_username(username)

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        creates and saves a Super User with the given
        email, username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must has is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must has is_superuser=True"))
        return self._create_user(email, username, password, **extra_fields)

    def create_user(
        self,
        email=None,
        username=None,
        password=None,
        **extra_fields
    ):
        """
        creates and saves a User with the given Email, Username and password.
        without Staff or SuperUser permissions.
        """
        extra_fields.setdefault('is_active', False)

        return self._create_user(email, username, password, **extra_fields)


# Define UserManager from ModelManager and QuerySet
UserManager = UserManager.from_queryset(UserQuerySet)
