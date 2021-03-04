# from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def time(request):
    time_now = datetime.now()
    days = time_now.day
    mounts = time_now.month
    years = time_now.year
    return HttpResponse(f'{days}-{mounts}-{years}')


def to_pow(request, number):
    return HttpResponse(f'{number ** 2}')
