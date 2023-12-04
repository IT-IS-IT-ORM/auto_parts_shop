from django.db import models
from user.models import User


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='类别名称')
    parent = models.ForeignKey(
        to='self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父类别')

    # 此函数将返回Category名 若有父类Category将一并返回
    def __str__(self):
        if self.parent:
            return f'{self.parent} {self.title}'
        else:
            return self.title

    class Meta:
        db_table = 'category'
        verbose_name = '商品类别'
        verbose_name_plural = '商品类别'


class Product(models.Model):
    '''商品模型类'''

    avaliable_types = (
        ('sm', 'Жеңіл автомобил'),
        ('md', 'Фургон'),
        ('lg', 'Үлкен жүк көлік'),
    )

    title = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    is_new = models.BooleanField()
    type = models.CharField(max_length=2, choices=avaliable_types, verbose_name='商品类型')
    views = models.IntegerField(default=0, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    # Sub Category ↓
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    applicable = models.ManyToManyField(Category, related_name='applicables')

    def __str__(self):
        return f'🎈 {self.title}'

    class Meta:
        db_table = 'product'
        verbose_name = '商品'
        verbose_name_plural = '商品'


class ProductImage(models.Model):
    image = models.FileField(upload_to='product', null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'📷 {self.product.title}'

    class Meta:
        db_table = 'product_image'
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'


class ProductComment(models.Model):
    content = models.CharField(max_length=256, verbose_name='评论内容')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user} - {self.product}'

    class Meta:
        db_table = 'product_comment'
        verbose_name = '商品评论'
        verbose_name_plural = '商品评论'
