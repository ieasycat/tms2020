import requests
from catdog.models import AnimalImage
from datetime import datetime


def getting_an_image(url, text):
    data = requests.get(url).json()
    context = {
        'data': data[text]
    }
    return context, data


def save_image(context, data, text, view):
    my_type = context['data'].split('.')[-1]
    animal = AnimalImage(url=data[text], species=view, data_crate=datetime.now(), image_type=my_type)
    animal.save()
