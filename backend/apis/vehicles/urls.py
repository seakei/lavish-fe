from rest_framework.routers import DefaultRouter

from .views import VehicleViewSet, BookingViewSet

app_name = 'apis.vehicles'

# Resources
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'bookings', BookingViewSet, basename='booking')

other_patterns = [
]

# Main entry point
urlpatterns = router.urls + other_patterns
