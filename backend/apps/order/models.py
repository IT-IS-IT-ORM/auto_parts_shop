from django.db import models
from user.models import User
from product.models import Product

# Create your models here.

class Order(models.Model):

    text = models.TextField(null=True)
    payment_status = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')

    def __str__(self):
        return str(self.product) + str(self.buyer)