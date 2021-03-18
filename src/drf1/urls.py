from django.urls import path
from drf1.views import APIProducts, APIProductDetail

urlpatterns = [
    path('products/', APIProducts.as_view(), name='products'),
    path('product/<int:pk>', APIProductDetail.as_view(), name='products'),
]
