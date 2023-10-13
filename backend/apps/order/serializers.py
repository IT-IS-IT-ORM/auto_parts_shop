from rest_framework import serializers

from order.models import Order
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    class Meta:
        model = Order
        fields = '__all__'