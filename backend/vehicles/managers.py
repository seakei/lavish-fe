from django.db import models


class BookingQueryset(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)


class BookingManager(models.Manager):
    pass


BookingManager = BookingManager.from_queryset(BookingQueryset)
