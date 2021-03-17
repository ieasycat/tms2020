from django.urls import path
from drf1.views import api_products, api_product_one

urlpatterns = [
    path('products/', api_products, name='products'),
    path('product/<int:pk>', api_product_one, name='products'),
]
