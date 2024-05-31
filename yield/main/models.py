from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, default='blé')  # Ensure the product name is unique

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=255, unique=True, default='casa')

class ProductRegion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='regions')
    region = models.ForeignKey(Region, on_delete=models.CASCADE,related_name='product_regions')
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('product', 'region')  # Ensure the combination of product and region is unique

    def __str__(self):
        return f"{self.product.name} in {self.region} - {self.quantity}"


