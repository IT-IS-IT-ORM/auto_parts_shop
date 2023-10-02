from django.db import models
from user.models import User 
# Create your models here.


class Category(models.Model):

    title = models.CharField(max_length=200, null=False, default='default category')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class ProductGallery(models.Model):

    # 图片field goes here，保存路径我不确定 先留着
    pass


class Product(models.Model):
    
    title = models.CharField(max_length=200, null=False, default='default product')
    price = models.FloatField(default=0, null=False)
    is_new = models.BooleanField(default=False)

    # gallery = models.ManyToManyField(ProductGallery)

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    applicable = models.ManyToManyField(Category, related_name='applicables', null=True)




class Comment(models.Model):

    text = models.TextField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.product)+' '+ str(self.user)