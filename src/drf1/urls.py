from django.urls import path
from drf1.views import api_products

urlpatterns = [
    path('products/', api_products, name='products'),
]
