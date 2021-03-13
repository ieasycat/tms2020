from django.shortcuts import render
import requests
from catdog.models import AnimalImage
from datetime import datetime

# Create your views here.


def catdog(request):
    return render(request, 'catdog.html')


def cats(request):
    data = requests.get('https://aws.random.cat/meow').json()
    context = {
        'data': data['file']
    }
    if request.method == 'GET':
        return render(request, 'cats.html', context)
    else:
        if request.POST.get('button') == 'save':
            my_type = context['data'].split('.')[-1]
            animal = AnimalImage(url=data['file'], species='cat', data_crate=datetime.now(), image_type=my_type)
            animal.save()
            return render(request, 'cats.html', context)


def dogs(request):
    data = requests.get('https://dog.ceo/api/breeds/image/random').json()
    context = {
        'data': data['message']
    }
    if request.method == 'GET':
        return render(request, 'dogs.html', context)
    else:
        if request.POST.get('button') == 'save':
            my_type = context['data'].split('.')[-1]
            animal = AnimalImage(url=data['message'], species='dog', data_crate=datetime.now(), image_type=my_type)
            animal.save()
            return render(request, 'dogs.html', context)
