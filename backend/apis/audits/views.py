# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from rest_framework import permissions
from rest_framework import viewsets

from .serializers import AuditSerializer

from auditlog.models import LogEntry


class AuditViewSet(viewsets.ModelViewSet):
    serializer_class = AuditSerializer
    queryset = LogEntry.objects.all()    
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('object_pk',)
    
    http_method_names = ['get', ]

    permission_classes = (permissions.IsAuthenticated, )