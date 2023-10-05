from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import (
    UserSerializer, LoginSerializer, RegisterSerializer, ChangePasswordSerializer, FavoriteSerializer)
from user.models import (User, Favorite
                         )

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
    authentication_classes = []

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
    authentication_classes = []

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


class FavoriteListAPIView(APIView):
    """
    My Favorite API
    """
    authentication_classes = [LoginRequiredAuthentication]

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_serializer_context(self):
        """
        update context object
        """
        context = super().get_serializer_context()
        context.update({'request': self.request})

        return context