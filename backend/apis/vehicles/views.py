# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.db.models import Prefetch

from rest_framework import permissions
from rest_framework import viewsets

from vehicles.models import Vehicle, Booking

from vehicles.services import handle_partner_and_booking

from .serializers import VehicleSerializer, BookingExtrasSerializer
from .filters import VehicleFilter, BookingFilter

UserModel = get_user_model()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter

    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.prefetch_related(
            Prefetch('bookings', queryset=Booking.objects.active())
        )

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     if self.action == 'list':
    #         context['exclude_fields'] = ['bookings']
    #     return context

    def perform_create(self, serializer):
        vehicle = serializer.save(created_by=self.request.user)
        handle_partner_and_booking(
            vehicle, validated_data=serializer.validated_data, **self.request.data
        )

    def perform_update(self, serializer):
        vehicle = serializer.save(updated_by=self.request.user)
        handle_partner_and_booking(
            vehicle, validated_data=serializer.validated_data, **self.request.data
        )


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingExtrasSerializer
    queryset = Booking.objects.all()
    filterset_class = BookingFilter

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        booking = serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        booking = serializer.save(updated_by=self.request.user)
