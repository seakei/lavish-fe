from rest_framework.routers import DefaultRouter

from .views import AuditViewSet

app_name = 'apis.audits'

# Resources
router = DefaultRouter()
router.register(r'audits', AuditViewSet, basename='audit')

other_patterns = [
]

# Main entry point
urlpatterns = router.urls + other_patterns
