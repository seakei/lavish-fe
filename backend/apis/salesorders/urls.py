# # -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SalesOrderViewSet, OrderViewSet, OrderItemViewSet, SignatureViewSet


app_name = 'apis.salesorders'

# Resources
router = DefaultRouter()
router.register(r'salesorders', SalesOrderViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'signatures', SignatureViewSet)

other_patterns = [
    path('test', SalesOrderViewSet.test_method),
 ]

# Main entry point
urlpatterns = router.urls + other_patterns
