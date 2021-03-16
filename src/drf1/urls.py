from django.urls import path
from drf1.views import api_products, api_products_one

urlpatterns = [
    path('products/', api_products, name='products'),
    path('product/<int:pk>', api_products_one, name='products'),
]
