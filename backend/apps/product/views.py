from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.

class ProductViewSet(ModelViewSet):

    authentication_classes = []


    queryset = Product.objects.all()
    serializer_class = ProductSerializer

        
class CategoryViewSet(ModelViewSet):

    authentication_classes = []


    queryset = Category.objects.all()
    serializer_class = CategorySerializer
