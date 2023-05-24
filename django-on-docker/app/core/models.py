from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    qty = models.IntegerField()
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Vendors(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)#Customer
    amount = models.FloatField()

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE) #One customer can place multiple orders, but one order will have one customer
    status = models.SmallIntegerField(default=0)#0=new, 1=processed etc.
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    noItems = models.IntegerField(default=0)#Number of items
    price = models.FloatField(default=0)#Total value of selected items
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)  
    qty = models.IntegerField()
    price = models.FloatField()

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)#Customer
    noItems = models.IntegerField(default=0)#Number of items
    price = models.FloatField(default=0)#Total value of selected items

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)  
    qty = models.IntegerField()
    price = models.FloatField()

    
    
