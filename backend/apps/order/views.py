from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from product.models import Product
from .models import Order
from .serializers import OrderSerializer

# Create your views here.


class OrderAPIView(APIView):

    # authentication_classes = []


    # queryset = Order.objects.all()
    # serializer_class = OrderSerializer


    def get(self, request):

        user_id =  request.GET['id']
        
        if user_id:
            user = User.objects.get(id=user_id)
            if int(user.role) == 1:
                order = Order.objects.filter(buyer=user)
            else:
                order = Order.objects.filter(seller=user)


        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

        
