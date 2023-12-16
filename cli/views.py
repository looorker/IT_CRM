from django.shortcuts import render, redirect
from django.http import HttpResponse

from cli.forms import *
from cli.models import *


# Create your views here.
def home(request):
    ivent = Meetup.objects.order_by('-start_date')

    context = {
        'ivent': ivent,
    }

    return render(request, 'cli/home.html', context=context)


def analisus(request):
    return render(request, 'cli/analisus.html')


def send(request):
    return render(request, 'cli/send.html')


def manage(request):
    return render(request, 'cli/manage.html')


def register(request):
    form = UserCreateForm()
    context = {
        'form': form,
    }

    if(request.method == 'POST'):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('manage')
            except:
                form.add_error(None, 'Ошибка создания пользователя.')

    return render(request, 'cli/register.html', context=context)


def event_add(request):
    form = EventCreateForm()
    context = {
        'form': form,
    }

    if(request.method == 'POST'):
        form = EventCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('manage')
            except:
                form.add_error(None, 'Ошибка создания ивента.')

    return render(request, 'cli/event_add.html', context=context)
