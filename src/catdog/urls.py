from django.urls import path
from catdog.views import catdog, cats, dogs

urlpatterns = [
    path('catdog', catdog, name='catdog'),
    path('cats', cats, name='cats'),
    path('dogs', dogs, name='dogs'),
]
