from django.urls import path
from .views import ProductViewSet, CategoryViewSet

from rest_framework import routers
from django.conf import settings


if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'category', CategoryViewSet)
router.register(r'', ProductViewSet)

urlpatterns = router.urls

urlpatterns += [
    # path('', ProductAPIView.as_view())
]
