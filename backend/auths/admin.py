from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .models import (
    User,
)


@admin.register(User)
class UserAdmin(UserAdmin):
    """
    User view for django admin.
    """
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', )
    list_filter = ('is_superuser', 'is_staff', 'is_active', )


admin.site.register(Permission)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
