from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda req: redirect('search/')),
    path('search/', views.product, name='search'),
]