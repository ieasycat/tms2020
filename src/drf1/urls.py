from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf1.views import APIProducts


route = DefaultRouter()
route.register('products', APIProducts)

urlpatterns = [
    path('', include(route.urls)),
]
