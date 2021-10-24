from django import forms

class ProductForm(forms.Form):
    seller = forms.CharField(max_length=100)
    universal_product_id = forms.CharField(max_length=200)