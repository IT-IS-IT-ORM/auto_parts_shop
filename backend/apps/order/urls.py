from django.urls import path
from order.views import OrderAPIView


from rest_framework import routers
from django.conf import settings


if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'order', OrderAPIView)


urlpatterns = router.urls
