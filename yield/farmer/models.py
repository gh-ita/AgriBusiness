from django.db import models
from django.contrib.auth.models import User
from main.models import Product  # Import Product model from main_app
from django.conf import settings

class Farmer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='farmers')  # Link to Product model
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

