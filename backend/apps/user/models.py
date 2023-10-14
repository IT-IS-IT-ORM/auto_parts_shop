from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.hashers import make_password


class User(models.Model):
    '''User model'''

    avaliable_roles = (
        ('0', '提供者'),
        ('1', '消费者')
    )

    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    fullname = models.CharField(max_length=30, verbose_name='全名')
    password = models.CharField(max_length=254, verbose_name='密码')
    role = models.CharField(max_length=1, choices=avaliable_roles, verbose_name='角色')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    class Meta:
        db_table = 'user'
        verbose_name = '系统用户'
        verbose_name_plural = '系统用户'

    def __str__(self):
        role_flag = '👑 ' if self.role == '0' else '💵'
        return f'({self.id}) {role_flag}{self.fullname}'

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    '''Пайдаланушыларды сақтамас бұрын құпия сөздерді шифрлау'''
    # pbkdf2_sha256$
    if not instance.password.startswith('pbkdf2_sha256$'):
        instance.password = make_password(instance.password)


class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.product}'

    class Meta:
        db_table = 'favorite'
        verbose_name = '收藏夹'
        verbose_name_plural = '收藏夹'