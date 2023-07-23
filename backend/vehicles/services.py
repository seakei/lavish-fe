from django.contrib.auth import get_user_model

from partners.models import BusinessPartner
from vehicles.models import Booking


UserModel = get_user_model()


def handle_partner_and_booking(vehicle, validated_data={}, **kwargs):
    vehicle.refresh_from_db()
    partner_uuid = kwargs.pop('uuid', None)

    partner_attrs = kwargs.get('partner', {})
    bookings = kwargs.get('bookings', {})

    if partner_attrs:
        value_remap = ['branch', 'role', 'profile_status']

        for i in value_remap:
            if i in partner_attrs.keys():
                partner_attrs[i] = validated_data.get('partner', {}).get(i)

        partner_uuid = partner_attrs.pop('uuid', None)
        if partner_uuid:
            partner = BusinessPartner.objects.get(pk=partner_uuid)
            for k, v in partner_attrs.items():
                setattr(partner, k, v)
            partner.save()
        else:
            partner = BusinessPartner.objects.create(**partner_attrs)
            partner.refresh_from_db()

        vehicle.partner = partner

    if bookings:
        for booking_attrs in bookings:
            booking_uuid = booking_attrs.pop('uuid', None)
            if booking_uuid:
                booking = Booking.objects.get(pk=booking_uuid)
                for k, v in booking_attrs.items():
                    setattr(booking, k, v)
                booking.save()
            else:
                Booking.objects.create(vehicle=vehicle, **booking_attrs)

    vehicle.save()
