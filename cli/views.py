import os

import pandas
from django.shortcuts import render, redirect
from . import mail_utils
from cli.forms import *
from cli.models import *
import pandas as pd
from django.views.generic import DetailView, UpdateView, DeleteView


#############################################
class MeetupUpdateView(UpdateView):
    model = Meetup
    template_name = 'cli/event_add.html'
    form_class = EventCreateForm

class MeetupDeliteView(DeleteView):
    model = Meetup
    template_name = 'cli/event_add.html'


class MeetupView(DetailView):
    model = Meetup
    template_name = 'cli/event_card.html'
    context_object_name = 'mt_card'


def home(request):
    ivent = Meetup.objects.order_by('-start_date')

    context = {
        'ivent': ivent,
    }

    return render(request, 'cli/home.html', context=context)


def analisus(request):
    return render(request, 'cli/analisus.html')


def send(request):
    form = SendMailForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            msg = form.cleaned_data.get('message')
            City = form.cleaned_data.get('city')
            Area = form.cleaned_data.get('area')
            Level = form.cleaned_data.get('level')
            subjects = User.objects.filter(city=City, area=Area, master=Level)
            s = mail_utils.Mailer()
            mail_array = []
            for sub in subjects:
                mail_array.append(sub.email)
            print(mail_array)
            s.send_mail(recipients_emails=mail_array, subject=title, msg_text=msg)

            form.add_error(None, 'Ошибка рассылки писем.')
    return render(request, 'cli/send.html', context)


def manage(request):
    return render(request, 'cli/manage.html')


def register(request):
    form = UserCreateForm()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        try:
            file = request.FILES['xls_data']
            handle_uploaded_file(file)

        except:
            pass

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

    if (request.method == 'POST'):
        form = EventCreateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('manage')
            except:
                form.add_error(None, 'Ошибка создания ивента.')

    return render(request, 'cli/event_add.html', context=context)


def handle_uploaded_file(f):
    with open('users.xls', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    parse_data()


def parse_data():
    df = pandas.read_excel('users.xlsx', sheet_name='Sheet1')
    print(df)
    df_m = df.values.tolist()
    for i in df_m:
        User.objects.create(name=i[0], sername=i[1], age=i[2], description=i[3] if i[3] != 'nan' else '', master=i[4],
                            area=i[5], city=i[6], email=i[7])
