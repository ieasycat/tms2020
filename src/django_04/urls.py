from django.urls import path
from django_04.views import info

urlpatterns = [
    path('info', info, name='info'),
]
