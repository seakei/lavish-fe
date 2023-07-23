from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import UserViewSet, ProfileViewSet

app_name = 'apis.auths'

# Resources
router = DefaultRouter()
router.register(r'auths', UserViewSet, basename='auth')

other_patterns = [
    path('api-token-auth/', obtain_jwt_token, name='token_obtain_pair'),
    path('api-token-refresh', refresh_jwt_token, name='token_refresh'),
    path('api-token-verify/', verify_jwt_token, name='token_verify'),
    path('me/', ProfileViewSet.as_view(), name='auth_me'),
]

# Main entry point
urlpatterns = router.urls + other_patterns
