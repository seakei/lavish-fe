from django_filters import rest_framework as filters

from partners.const import BRANCH_CHOICES

from vehicles.models import Vehicle, Booking


class VehicleFilter(filters.FilterSet):
    # https://django-filter.readthedocs.io/en/stable/ref/filters.html#datetimefromtorangefilter
    booking_date = filters.DateTimeFromToRangeFilter(
        field_name='bookings__booking_date'
    )

    branch = filters.CharFilter(method='filter_branch')

    class Meta:
        model = Vehicle
        # fields = ('is_active', 'booking_date', )
        fields = {
            'is_active': ['exact'],
            'car_plate': ['istartswith'],
        }

    @staticmethod
    def filter_branch(queryset, name, value):
        values = (x[0] for x in BRANCH_CHOICES if x[1] == value)
        return queryset.filter(branch__in=values)


class BookingFilter(filters.FilterSet):
    booking_date = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Booking
        fields = (
            'is_active',
            'booking_date',
        )
