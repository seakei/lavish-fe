from django.contrib.auth import get_user_model

from rest_framework import serializers

from ..partners.serializers import BaseBusinessPartnerSerializer


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    partner = BaseBusinessPartnerSerializer()

    class Meta:
        model = UserModel
        fields = (
            'uuid', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'force_change_password',
            'created_by', 'updated_by', 'partner'
        )

        read_only = ('id', )

        extra_kwargs = {
            'username': {"required": True},
            'first_name': {"required": True},
            'last_name': {"required": True},
            'password': {"write_only": True},
        }

    def create(self, validated_data):
        validated_data.pop('partner', None)
        password = ''

        if validated_data.get("password"):
            password = validated_data.pop('password')
            to_set_password = True

        user = super().create(validated_data)

        if to_set_password:
            user.set_password(password)
            user.save()

        return user

    def update(self, instance, validated_data):
        validated_data.pop('partner', None)
        if validated_data.get("password"):
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
