from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

from utils.authentication import LoginRequiredAuthentication


class OrderAPIView(ModelViewSet):

    authentication_classes = [LoginRequiredAuthentication]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == '1':
            return Order.objects.filter(buyer=user)
        else:
            return Order.objects.filter(product__seller=user)
