from django.db import models
from django.db.models.query import QuerySet

class SalesOrderCustomManager(models.Manager):
    pass
    
class SalesOrderQuerySet(models.QuerySet):  
    def salesorders_active_only(self):
        return self.filter(is_active=True,)
    
class OrderCustomManager(models.Manager):
    pass

class OrderQuerySet(models.QuerySet):    
    def orders_active_only(self):
        return self.filter(is_active=True,)

class OrderItemCustomManager(models.Manager):
    pass

class OrderItemQuerySet(models.QuerySet):
    def orderitems_active_only(self):
        return self.filter(is_active=True,)
    
class SignatureCustomManager(models.Manager):
    def get_signature(self):
        return SignatureQuerySet.signature_queryset_method()

class SignatureQuerySet(models.QuerySet):
    def signature_queryset_method(self):
        return self.get()

    
SalesOrderManager = SalesOrderCustomManager.from_queryset(SalesOrderQuerySet)
OrderManager = OrderCustomManager.from_queryset(OrderQuerySet)
ItemManager = OrderItemCustomManager.from_queryset(OrderItemQuerySet)
SignatureManager = SignatureCustomManager.from_queryset(SignatureQuerySet)