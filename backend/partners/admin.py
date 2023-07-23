from django.contrib import admin

from .models import BusinessPartner


@admin.register(BusinessPartner)
class BusinessPartnerAdmin(admin.ModelAdmin):
    """
    Business Partner Django admin display.

    Richard, 23.05.2023
    """
    list_display = (
        'uuid', 'name', 'category',
        'created_at',
    )
    list_filter = ('category', )
    search_fields = (
        'uuid', 'name', 'user__email', 'user__username',
    )
