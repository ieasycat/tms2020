from django.shortcuts import render

# Create your views here.


def catdog(request):
    if request.method == 'GET':
        return render(request, 'catdog.html')
