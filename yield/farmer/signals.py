from django.dispatch import receiver
from base.signals import user_registered
from .models import Farmer, Product

@receiver(user_registered)
def create_user_table(sender, **kwargs):
    user = kwargs['user']
    products = Product.objects.all()  # Fetch all products from the Product table

    for product in products:
        Farmer.objects.create(user=user, product=product, quantity=0)
