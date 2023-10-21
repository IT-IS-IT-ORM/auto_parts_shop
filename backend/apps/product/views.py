from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        """
        update context object
        """
        context = super().get_serializer_context()
        context.update({'request': self.request})

        return context


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
