from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer

# Create your views here.


class OrderViewSet(ModelViewSet):

    authentication_classes = []


    queryset = Order.objects.all()
    serializer_class = OrderSerializer

        
