from django.urls import path
from django_04.views import info, full_form

urlpatterns = [
    path('info', info, name='info'),
    path('full_form', full_form, name='full form')
]
