from rest_framework import serializers

from .models import Order

from user.models import User
from user.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'