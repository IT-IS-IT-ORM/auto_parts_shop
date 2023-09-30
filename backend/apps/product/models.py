from django.db import models

# Create your models here.

class Product(models.Model):
    
    title = models.CharField(max_length=200, null=False, default='default product')
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return self.title