from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product

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

    def create(self, request, *args, **kwargs):
        product = Product.objects.get(id=request.data.get('product_id'))
        order = Order.objects.create(price=product.price, product=product, buyer=request.user)
        serializer = OrderSerializer(instance=order, context={'request': request})

        return Response(data=serializer.data)
