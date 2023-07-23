# -*- coding: utf-8 -*-
from django.urls import include, path


app_name = 'apis'

services_patterns = [
    path('auth-service/', include('apis.auths.urls', namespace='auth-service')),
    path('partner-service/', include('apis.partners.urls', namespace='partner-service')),
    path('salesorder-service/', include('apis.salesorders.urls', namespace='salesorder-service')),
    path('vehicle-service/', include('apis.vehicles.urls', namespace='vehicle-service')),
    path('audit-service/', include('apis.audits.urls', namespace='audit-service')),
    path('inspection-service/', include('apis.inspections.urls', namespace='inspection-service')),
]

urlpatterns = services_patterns
