from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Region, ProductRegion

@receiver(post_save, sender=Product)
def create_product_regions_for_product(sender, instance, created, **kwargs):
    if created:
        regions = Region.objects.all()
        for region in regions:
            ProductRegion.objects.create(product=instance, region=region, quantity=0)

@receiver(post_save, sender=Region)
def create_product_regions_for_region(sender, instance, created, **kwargs):
    if created:
        products = Product.objects.all()
        for product in products:
            ProductRegion.objects.create(product=product, region=instance, quantity=0)
