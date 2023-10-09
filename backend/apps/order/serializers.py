from rest_framework import serializers

from .models import Order
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'