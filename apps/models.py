from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from .storage_backends import StaticStorage

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'store_product'  # Specify the table name explicitly

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_price(self):
        """Calculate the total price for this cart item."""
        return self.product.price * self.quantity

class AdminUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords ideally

    def __str__(self):
        return self.username

