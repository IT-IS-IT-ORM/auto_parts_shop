from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


from utils.authentication import LoginRequiredAuthentication

# Create your views here.


class OrderAPIView(ModelViewSet):

    authentication_classes = [LoginRequiredAuthentication]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def get_queryset(self):
       #用户是个球
       if int(self.request.user.role) == 1:
        return Order.objects.filter(buyer=self.request.user)
       else:
        return Order.objects.filter(product__seller=self.request.user)

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True, context={
                                     'user': self.request.user})
        return Response(serializer.data)
