import logging

from django.shortcuts import render

from . import models
from . import filters

logger = logging.getLogger(__name__)


def product(request):
    """ Product Search 
    
    **Template**

    :template:`product/product__page.html`
    
    """
    

    product__filter = filters.ProductFilter(
        request.GET, 
        queryset=models.Product.objects.all()
    )

    return render(
        request, "product/product__page.html",
        {
            "products": product__filter.qs,
            "product__filter": product__filter
        }
    )
    
    
