from django import forms

from .models import *

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group mx-sm-3 mb-2'}),
            'sername': forms.TextInput(attrs={'class': 'form-group mx-sm-3 mb-2'}),
        }

class EventCreateForm(forms.ModelForm):

    class Meta:
        model = Meetup
        fields = ['name', 'area', 'description', 'start_date']