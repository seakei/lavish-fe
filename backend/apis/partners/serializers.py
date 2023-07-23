from rest_framework import serializers

from partners.models import (
    BusinessPartner,
)

from partners.const import ROLE_CHOICES, CATEGORY_CHOICES, PROFILE_STATUS_CHOICES, BRANCH_CHOICES

from ..fields import ChoiceField


class BaseBusinessPartnerSerializer(serializers.ModelSerializer):
    role = ChoiceField(choices=ROLE_CHOICES, required=False)
    category = ChoiceField(choices=CATEGORY_CHOICES, required=False)
    profile_status = ChoiceField(choices=PROFILE_STATUS_CHOICES, required=False)
    branch = ChoiceField(choices=BRANCH_CHOICES, required=False)

    class Meta:
        model = BusinessPartner
        fields = '__all__'

        read_only = ('id', 'number', )

        extra_kwargs = {
            'phone_number': {"required": True},
        }
