from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

from partners.const import BRANCH_CHOICES

UserModel = get_user_model()


class UserFilter(filters.FilterSet):
    """The filter set performs field lookups on User model
    """

    name = filters.CharFilter(field_name='partner__name', lookup_expr='icontains')
    is_active = filters.CharFilter(field_name='is_active')
    role = filters.CharFilter(field_name='partner__role')
    branch = filters.CharFilter(method='filter_branch')

    class Meta:
        model = UserModel
        fields = [
            'partner__name',
            'is_active',
            'role',
            'branch'
        ]

    @staticmethod
    def filter_branch(queryset, name, value):
        values = (x[0] for x in BRANCH_CHOICES if x[1] == value)
        return queryset.filter(partner__branch__in=values)
