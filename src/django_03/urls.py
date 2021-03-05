from django.urls import path
from django_03.views import check_word, home_page

urlpatterns = [path('my_word/<word>', check_word, name='check_word'),
               path('home_page', home_page, name='home_page'),
               ]
