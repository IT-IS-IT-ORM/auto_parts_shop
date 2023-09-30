from django.db import models
from user.models import User 
# Create your models here.

class Product(models.Model):
    
    title = models.CharField(max_length=200, null=False, default='default product')
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):

    text = models.TextField(null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.product)+' '+ str(self.user)