# -*- coding: utf-8 -*-
from django_filters import rest_framework as filters

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import UserFilter
from .serializers import UserSerializer
from auths.services import create_or_update_partner_models_from_user

from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        user = serializer.save(created_by=self.request.user, force_change_password=True)
        create_or_update_partner_models_from_user(user, **serializer.validated_data)

    def perform_update(self, serializer):
        user = serializer.save(updated_by=self.request.user)
        create_or_update_partner_models_from_user(user, is_update=True, **serializer.validated_data)


class ProfileViewSet(APIView):
    serializer_class = UserSerializer
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
