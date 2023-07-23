# # -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import InspectionViewSet, InspectionSignatureViewSet, InspectionUploadViewset


app_name = 'apis.inspections'

# Resources
router = DefaultRouter()
router.register(r'inspections', InspectionViewSet)
router.register(r'inspectionsignatures', InspectionSignatureViewSet)
router.register(r'inspectionuploads', InspectionUploadViewset)

other_patterns = []

# Main entry point
urlpatterns = router.urls + other_patterns
