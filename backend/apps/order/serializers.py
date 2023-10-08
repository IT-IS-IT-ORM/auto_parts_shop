from rest_framework import serializers

from .models import Order

from product.models import Product

from user.models import User
from user.serializers import UserSerializer



class OrderSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):

        print(instance)
        print(type(instance))
        orders = super().to_representation(instance)
        print(orders)

        user = self.context.get('user')


        for order in orders:
            print(order)

        if int(user.role) == 1:
            order = Order.objects.filter(buyer=user)
            print('I AM BUYER')
            # 烂尾妈的
            # 目标 获取卖家的订单 Order里不创建seller字段的情况下
        # else:
        #     product = Product.objects.filter(seller=user)

        #     for p in product:
                
        #     my_order = Order.objects.filter(product=)
        #     print('I AM SELLER')



        return orders
        