from django.urls import path
from .views import OrderViewSet

from rest_framework import routers
from django.conf import settings


if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'', OrderViewSet)

urlpatterns = router.urls


urlpatterns += [
    # path('', ProductAPIView.as_view())
]
