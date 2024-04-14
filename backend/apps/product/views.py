from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

from utils.authentication import LoginRequiredAuthentication


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [JSONParser, MultiPartParser, FileUploadParser]

    def get_serializer_context(self):
        """
        update context object
        """
        context = super().get_serializer_context()
        context.update({"request": self.request})

        return context

    def list(self, request, *args, **kwargs):
        query_params = request.query_params
        type = query_params.get("type", None)
        has_image = query_params.get("hasImage", None)
        is_new = query_params.get("isNew", None)
        price_range = query_params.get("priceRange", None)
        categories = query_params.get("categories", None)
        sub_categories = query_params.get("subCategories", None)

        print("request.query_params: ", query_params)
        print("type: ", type)
        print("has_image: ", has_image)
        print("is_new: ", is_new)
        print("price_range: ", price_range)
        print("categories: ", categories)
        print("sub_categories: ", sub_categories)
        # 如果 type 为 null, 就不需要 filter
        products = Product.objects.filter(type=type)

        return super().list(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        grouped_categories = []
        categories = super().list(request, *args, **kwargs).data

        for category in categories:
            parent_id = category.get("parent")
            if parent_id is None:
                category["sub_categories"] = []
                grouped_categories.append(category)
                continue

            for parent_category in grouped_categories:
                if parent_category.get("id") == parent_id:
                    parent_category.get("sub_categories").append(category)

        return Response(data=grouped_categories)


class MyProductAPI(APIView):
    authentication_classes = [LoginRequiredAuthentication]

    def get(self, request):
        product_list = Product.objects.filter(seller=request.user)
        product_list_serialized = ProductSerializer(
            instance=product_list, many=True,
            context={'request': request}).data

        return Response(data=product_list_serialized)
