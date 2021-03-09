from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.


def check_word(request, word):
    if len(word) % 2 == 0:
        return HttpResponse(f'{word[::2]}')
    else:
        return redirect('home_page')


def home_page(request):
    return HttpResponse("Hello, it's main page!")
