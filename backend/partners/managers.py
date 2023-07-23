from django.db import models

from .const import PERSON


class BusinessPartnerQueryset(models.QuerySet):
    def no_root(self, partner):
        qs = self.filter(
            is_active=True,
            category=PERSON,
            hierarchy__in=partner.get_hierarchies()
        ).exclude(user__username='root')

        return qs


class BusinessPartnerManager(models.Manager):
    pass


BusinessPartnerManager = BusinessPartnerManager.from_queryset(BusinessPartnerQueryset)
