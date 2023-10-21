from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import (
    UserSerializer, LoginSerializer, RegisterSerializer, ChangePasswordSerializer)
from user.models import (User, Favorite)
from product.serializers import FavoriteSerializer, SetFavoriteSerializer

from utils.jwt import create_jwt
from utils.authentication import LoginRequiredAuthentication


class UserViewSet(ModelViewSet):
    """
    User API 
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        """
        update context object
        """
        context = super().get_serializer_context()
        context.update({'request': self.request})

        return context


class LoginAPIView(APIView):
    """
    Login API
    """
    

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.is_correct()
        token = create_jwt({'uid': user.id})

        data = UserSerializer(instance=user).data
        data['token'] = token

        return Response({'data': data, 'Formatted': 1})


class RegisterAPIView(APIView):
    """
    Register API
    """
    

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.register()
        token = create_jwt({'uid': user.id})

        data = UserSerializer(instance=user).data
        data['token'] = token

        return Response({'data': data, 'Formatted': 1})


class ChangePasswordAPIView(APIView):
    """
    Change password API
    """
    authentication_classes = [LoginRequiredAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'user': self.request.user})

        serializer.is_valid(raise_exception=True)
        user = serializer.change_password()

        data = UserSerializer(instance=user).data
        return Response({'data': data, 'Formatted': 1})


class FavoriteAPIView(APIView):
    """
    Favorite API
    """
    authentication_classes = [LoginRequiredAuthentication]

    def get(self, request):
        # 获取当前用户的收藏列表
        user_id = request.user.id
        favorites = Favorite.objects.filter(user_id=user_id)

        # 序列化收藏列表
        favorites_data = FavoriteSerializer(favorites, many=True,
                                            context={'request': self.request}).data

        # 构建响应
        response_data = {'data': favorites_data, 'Formatted': 1}
        return Response(response_data)

    def post(self, request):
        serializer = SetFavoriteSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.create()

        return Response({'data': None, 'Formatted': 1})

    def delete(self, request):
        serializer = SetFavoriteSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.delete()

        return Response({'data': None, 'Formatted': 1})
