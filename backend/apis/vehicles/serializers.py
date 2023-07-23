from django.contrib.auth import get_user_model

from rest_framework import serializers

from vehicles.models import Vehicle, Booking

from ..partners.serializers import BaseBusinessPartnerSerializer

from partners.const import BRANCH_CHOICES

from ..fields import ChoiceField


UserModel = get_user_model()


class BaseBookingSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )
    updated_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = Booking
        exclude = ('vehicle',)

        read_only = ('id', 'number')


class BookingExtrasSerializer(BaseBookingSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )
    updated_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )
    partner = BaseBusinessPartnerSerializer()
    bookings = BaseBookingSerializer(many=True)
    branch = ChoiceField(choices=BRANCH_CHOICES, required=False)

    class Meta:
        model = Vehicle
        fields = (
            'uuid',
            'is_active',
            'car_plate',
            'car_brand',
            'package',
            'remarks',
            'branch',
            'partner',
            'bookings',
            'created_by',
            'updated_by',
            'number',
        )

        read_only = ('id',)

        extra_kwargs = {
            'car_plate': {"required": True},
        }

    # def get_fields(self):
    #     fields = super().get_fields()

    #     exclude_fields = self.context.get('exclude_fields', [])
    #     for field in exclude_fields:
    #         # providing a default prevents a KeyError
    #         # if the field does not exist
    #         fields.pop(field, default=None)

    #     return fields

    def validate_car_plate(self, value):
        vehicle_qs = Vehicle.objects.filter(car_plate__icontains=value)
        if vehicle_qs.exists():
            raise serializers.ValidationError("Car plate already exists!")

        return value

    def create(self, validated_data):
        validated_data.pop('partner', None)
        validated_data.pop('bookings', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('partner', None)
        validated_data.pop('bookings', None)
        return super().update(instance, validated_data)
