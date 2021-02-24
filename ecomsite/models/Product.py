from django.db import models
from .categories import Category
# Create your models here.
class Product(models.Model):
    Name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    fk=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Description=models.CharField(max_length=200,default='')
    Image=models.ImageField(upload_to='uploads/products/')
