import django_filters

from . import models


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = models.Product
        fields = ("seller", "universal_product_id", "seller_product_id", )
