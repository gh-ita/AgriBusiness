from django.contrib import admin
from .models import Product, Region, ProductRegion

# Register your models here.
admin.site.register(Product)
admin.site.register(Region)
admin.site.register(ProductRegion)