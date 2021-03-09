from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django_04.form import UserForm

# Create your views here.


def info(request):
    template = loader.get_template('info.html')
    response = template.render({}, request)
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        old = request.POST.get('old')
        with open('django_04/log_django.txt', 'a') as log_file:
            log_file.writelines([f'First name: {first_name}\n'
                                 f'Last name: {last_name}\n'
                                 f'Old: {old}\n\n'])
    return HttpResponse(response)


def full_form(request):
    if request.method == 'GET':
        context = {'form': UserForm()}
        return render(request, 'django_06_form.html', context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd.get('firstname')
            last_name = cd.get('lastname')
            old = cd.get('old')
            context = {
                'firstname': first_name,
                'lastname': last_name,
                'old': old,
            }
            return render(request, 'django_06_display.html', context)
        errors = form.errors
        return HttpResponse(f'errors is {errors}')
