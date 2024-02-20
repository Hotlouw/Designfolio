from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    id = models.CharField(primary_key=True,max_length=7)
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(null = True, blank = True, upload_to='images/')
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.FloatField()
    price = models.FloatField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
class UserProfile(models.Model):
    username = models.CharField(max_length=50, default = "*")
    password = models.CharField(max_length=50, default="*")

    def __str__(self):
        return self.username        