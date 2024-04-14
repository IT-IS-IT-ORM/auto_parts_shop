from rest_framework import serializers

from product.models import Product, Category, ProductImage
from user.models import User, Favorite
from user.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    applicable = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        product = super().to_representation(instance)
        user = self.context.get('request').user

        subCategory = Category.objects.get(id=product['category'])
        category = Category.objects.get(id=subCategory.parent.id)
        categories = []
        categories.append(category)
        categories.append(subCategory)

        seller_id = int(product['seller'])
        product['seller'] = UserSerializer(User.objects.get(id=seller_id)).data

        # category自定义
        product['category'] = CategorySerializer(categories, many=True).data

        # gallery自定义
        gallery = ProductImage.objects.filter(product=product['id'])
        product['gallery'] = list(
            map(
                lambda image: ProductImageSerializer(
                    instance=image, context=self.context).data, gallery
            )
        )

        # is_favorite自定义
        product['is_favorite'] = False
        if user.is_authenticated:
            product['is_favorite'] = Favorite.objects.filter(
                product=product['id'], user=user).exists()

        # applicable自定义
        applicable = []
        def is_not_empty_string(str_id): return str_id != ''
        applicable_ids = filter(is_not_empty_string,
                                product['applicable'].split(','))

        for str_id in applicable_ids:
            category = Category.objects.get(id=int(str_id))
            applicable.append(CategorySerializer(instance=category).data)

        product['applicable'] = applicable

        return product

    def create(self, validated_data):
        product = super().create(validated_data)

        for file in self.context['request'].FILES.getlist('gallery'):
            ProductImage.objects.create(image=file, product=product).save()

        return product


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=ProductImage.objects.all(), write_only=True)

    class Meta:
        model = ProductImage
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image)


class FavoriteSerializer(serializers.Serializer):
    '''用于获取收藏夹列表'''
    product = ProductSerializer()
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)

    def to_representation(self, instance):
        favorite = super().to_representation(instance)
        return favorite['product']


class SetFavoriteSerializer(serializers.Serializer):
    '''用于新增/删除收藏'''
    product = serializers.IntegerField(write_only=True)

    def create(self):
        user = self.context.get('user')
        product_id = self.initial_data['product']
        product = Product.objects.get(id=product_id)

        return Favorite.objects.create(product=product, user=user)

    def delete(self):
        user = self.context.get('user')
        product_id = self.initial_data['product']

        Favorite.objects.get(user=user, product=product_id).delete()
