# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from .views import BusinessPartnerViewSet


app_name = 'apis.partners'

# Resources
router = DefaultRouter()
router.register(r'partners', BusinessPartnerViewSet, basename='partner')

other_patterns = []

# Main entry point
urlpatterns = router.urls + other_patterns
