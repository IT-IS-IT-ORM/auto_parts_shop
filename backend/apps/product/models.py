from django.db import models
from user.models import User 
import os
from uuid import uuid4

# Create your models here.

def wrapper(instance, filename):
    ext = filename.split('.')[-1]
        # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
     # return the whole path to the file
    return os.path.join('products', filename)


class Category(models.Model):

    title = models.CharField(max_length=200, null=False, default='default category')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


    # 此函数将返回Category名 若有父类Category将一并返回
    def __str__(self):
        if self.parent:
            return str(self.parent)+' '+str(self.title)
        else:
            return str(self.title)

class ProductGallery(models.Model):

    # 图片field goes here，保存路径我不确定 先留着
    
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=wrapper, null=True, max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    
    title = models.CharField(max_length=200, null=False, default='default product')
    price = models.FloatField(default=0, null=False)
    is_new = models.BooleanField(default=False)

    gallery = models.ManyToManyField(ProductGallery, null=True, blank=True)

    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    applicable = models.ManyToManyField(Category, related_name='applicables')


    def __str__(self):
        return self.title
        

class Comment(models.Model):

    text = models.TextField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.product)+' '+ str(self.user)