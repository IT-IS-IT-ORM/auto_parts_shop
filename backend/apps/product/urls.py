from django.urls import path
from product.views import ProductViewSet, CategoryViewSet

from rest_framework import routers
from django.conf import settings


if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = router.urls
