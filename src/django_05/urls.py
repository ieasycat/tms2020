from django.urls import path
from django_05.views import form

urlpatterns = [
    path('form', form, name='form')
]
