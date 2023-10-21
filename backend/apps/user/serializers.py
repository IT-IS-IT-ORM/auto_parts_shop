from django.contrib.auth.hashers import check_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User

from utils.custom_exception import CustomException


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    phone = serializers.CharField(
        label='手机号', max_length=11, trim_whitespace=True, validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message='Телефон тіркелген')
        ])
    fullname = serializers.CharField(
        label='全名', max_length=30, trim_whitespace=True)
    password = serializers.CharField(
        label='密码', write_only=True, max_length=254, trim_whitespace=True)
    role = serializers.ChoiceField(label='角色', choices=User.avaliable_roles)
    create_time = serializers.DateTimeField(
        label='注册时间', read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label='手机号', max_length=11, trim_whitespace=True)
    password = serializers.CharField(
        label='密码', write_only=True, max_length=254, trim_whitespace=True)

    def is_correct(self):
        """Жүйеге кіру деректерінің дұрыстығын тексеру"""
        phone = self.initial_data['phone']
        password = self.initial_data['password']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            raise CustomException(message='Телефон нөмір тіркелмеген')

        if not check_password(password, user.password):
            raise CustomException(message='Қате құпиясөз')

        return user


class RegisterSerializer(serializers.Serializer):
    fullname = serializers.CharField(
        label='全名', max_length=30, trim_whitespace=True)
    phone = serializers.CharField(
        label='手机号', max_length=11, trim_whitespace=True)
    password = serializers.CharField(
        label='密码', write_only=True, max_length=254, trim_whitespace=True)
    role = serializers.ChoiceField(label='角色', choices=User.avaliable_roles)

    def register(self):
        """Жүйеге кіру деректерінің дұрыстығын тексеру"""
        user = None
        phone = self.initial_data['phone']
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            pass

        if user:
            raise CustomException(message='Телефон тіркелген')

        fullname = self.initial_data['fullname']
        password = self.initial_data['password']
        role = self.initial_data['role']
        user = User.objects.create(
            phone=phone,
            fullname=fullname,
            password=password,
            role=role)

        return user


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        label='旧密码', write_only=True, max_length=254, trim_whitespace=True)
    new_password = serializers.CharField(
        label='新密码', write_only=True, max_length=254, trim_whitespace=True)

    def change_password(self):
        user = self.context.get('user')
        password = self.initial_data['password']
        new_password = self.initial_data['new_password']

        if not check_password(password, user.password):
            raise CustomException(message='Ескі құпиясөз қате')

        user.password = new_password
        user.save()
        return user
