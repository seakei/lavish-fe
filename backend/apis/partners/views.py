# -*- coding: utf-8 -*-
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import BaseBusinessPartnerSerializer

from partners.models import BusinessPartner


class BusinessPartnerViewSet(viewsets.ModelViewSet):
    serializer_class = BaseBusinessPartnerSerializer
    queryset = BusinessPartner.objects.all()

    permission_classes = (permissions.IsAuthenticated, )


class ProfileViewSet(APIView):
    serializer_class = BaseBusinessPartnerSerializer
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.request.user.partner)
        return Response(serializer.data, status=status.HTTP_200_OK)
