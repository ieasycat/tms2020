from django.shortcuts import render
from catdog.business_logic import getting_an_image, save_image

# Create your views here.


def catdog(request):
    return render(request, 'catdog.html')


def cats(request):
    context, data = getting_an_image(url='https://aws.random.cat/meow', text='file')

    if request.method == 'GET':
        return render(request, 'cats.html', context)
    else:
        if request.POST.get('button') == 'save':
            save_image(context, data, text='file', view='cat')
            return render(request, 'cats.html', context)


def dogs(request):
    context, data = getting_an_image(url='https://dog.ceo/api/breeds/image/random', text='message')

    if request.method == 'GET':
        return render(request, 'dogs.html', context)
    else:
        if request.POST.get('button') == 'save':
            save_image(context, data, text='message', view='dog')
            return render(request, 'dogs.html', context)
