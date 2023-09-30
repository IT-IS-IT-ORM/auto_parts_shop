from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductViewSet(ModelViewSet):

    authentication_classes = []


    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get(self, request):

    #     products = Product.objects.all()
    #     print(products)
    #     serializer = ProductSerializer(products, many=True)
    #     print(serializer.data)
    #     data = serializer.data

    #     return Response({'data':data})
        
