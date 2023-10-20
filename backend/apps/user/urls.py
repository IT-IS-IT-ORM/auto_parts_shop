from django.urls import path
from rest_framework import routers
from django.conf import settings

from user.views import UserViewSet, LoginAPIView, RegisterAPIView, ChangePasswordAPIView, FavoriteAPIView

if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'user', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    # Login API
    path('auth/login/', LoginAPIView.as_view()),
    # Register API
    path('auth/register/', RegisterAPIView.as_view()),
    # Change password API
    path('auth/change-password/', ChangePasswordAPIView.as_view()),
    # Favorite API
    path('favorite/', FavoriteAPIView.as_view()),
]

app_name = 'user'