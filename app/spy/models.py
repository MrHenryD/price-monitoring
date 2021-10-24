from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of Seller")
    active = models.BooleanField(help_text="Whether seller is still operating")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}{'' if self.active else ' (INACTIVE)' }"

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    universal_product_id = models.CharField(max_length=200, help_text="Universal product identifier")
    seller_product_id = models.CharField(max_length=200, help_text="Product identifier")
    name = models.CharField(max_length=200, null=True, help_text="Name of product")
    description = models.CharField(max_length=500, null=True, help_text="General description about the product")
    active = models.BooleanField(default=True, help_text="Whether we support monitoring the product")
    update_frequency = models.IntegerField(default=7, help_text="How frequent to check price changes (days)")
    price = models.FloatField(help_text="Seller's price of product")
    product_url = models.CharField(max_length=500, help_text="Reference to original product page")
    image_url = models.CharField(max_length=500, null=True, help_text="Reference to product image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.seller} {self.name}"