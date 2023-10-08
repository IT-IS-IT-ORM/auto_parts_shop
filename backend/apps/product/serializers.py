from rest_framework import serializers

from .models import Product, Category

from user.models import User, Favorite
from user.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):


        product = super().to_representation(instance)

        seller =  User.objects.get(id=product['seller'])
        
        subCategory = Category.objects.get(id=product['category'])
        category = Category.objects.get(id=subCategory.parent.id)
        categories = []
        categories.append(category)
        categories.append(subCategory)


        product['seller'] = UserSerializer(seller).data
        #消除token
        del product['seller']['token']

        # category自定义
        product['category'] = CategorySerializer(categories, many=True).data
        

        # applicable里自定义 没有用到serializer 而是调用Model里的__str__函数
        for index, item in enumerate(product['applicable']):
            applicable = Category.objects.get(id=item)
            product['applicable'][index] = {'id': applicable.id, 'title':str(applicable)}

        return product
    

class FavoriteSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'