import os
import pandas
from django.conf import settings
from django.db.models import Q, Max
from django.http import StreamingHttpResponse, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import mail_utils
from cli.forms import *
from cli.models import *
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView


#############################################
class UserListView(ListView):
    model = User
    template_name = 'cli/users.html'
    context_object_name = 'users'


class UserView(DetailView):
    model = User
    template_name = 'cli/user_card.html'
    context_object_name = 'usr'


class UserUpdateView(UpdateView):
    model = User
    fields = ['name', 'sername', 'age', 'description', 'master', 'area', 'city', 'email']
    template_name = 'cli/register.html'
    success_url = reverse_lazy('users')


class UserDeliteView(DeleteView):
    model = User
    template_name = 'cli/event_del.html'
    success_url = reverse_lazy('users')
    context_object_name = 'mt'


class UserSearchView(ListView):
    model = User
    template_name = 'cli/users.html'
    context_object_name = 'users'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = User.objects.filter(
            Q(name__icontains=query) | Q(sername__icontains=query)
        )
        return object_list


class MeetupAdd(CreateView):
    model = Meetup
    form_class = EventCreateForm
    template_name = 'cli/event_add.html'
    success_url = reverse_lazy('home')


class MeetupUpdateView(UpdateView):
    model = Meetup
    fields = ['name', 'area', 'description', 'start_date']
    template_name = 'cli/event_add.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs


class MeetupDeliteView(DeleteView):
    model = Meetup
    template_name = 'cli/event_del.html'
    success_url = reverse_lazy('home')
    context_object_name = 'mt'


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
    passed_events = Meetup.objects.filter(start_date__lte=timezone.now())
    running_events = Meetup.objects.filter(start_date__gte=timezone.now())
    users = User.objects.all()
    middle_age = 0
    users_c = 0
    for u in users:
        middle_age += u.age
        users_c += 1
    middle_age = middle_age/users_c
    n_passed_events = 0
    n_running_events = 0
    n_events = 0
    e_names = []
    passed_names = []
    running_names = []
    for e in passed_events:
        passed_names.append(e.name)
        n_passed_events += 1
    for e in running_events:
        running_names.append(e.name)
        n_running_events += 1
    passed_p = n_passed_events / (n_passed_events + n_running_events) * 100



    context = {
        'passed_e': n_passed_events,
        'running_e': n_running_events,
        'passed_p': round(passed_p, 1),
        'middle_age': round(middle_age, 0),
    }

    return render(request, 'cli/analisus.html', context)


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


# def event_add(request):
#     form = EventCreateForm()
#     context = {
#         'form': form,
#     }
#
#     if (request.method == 'POST'):
#         form = EventCreateForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('manage')
#             except:
#                 form.add_error(None, 'Ошибка создания ивента.')
#
#     return render(request, 'cli/event_add.html', context=context)


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


def download(request, path='test.xlsx'):
    print(0)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(file_path)
    if os.path.exists(file_path):
        print(1)
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
