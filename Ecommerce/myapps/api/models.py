from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class Customer(AbstractUser):
    uid = models.UUIDField(editable=False, default=uuid4)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    # contact = PhoneNumberField()
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.first_name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    
    def __str__(self):
        return f"Order {self.id}"
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return f'{self.quantity} - {self.product.name}'
    
    def price(self):
        price = self.product.price * self.quantity
        return price
    
       
    
    

