from django.forms import ModelForm
from .models import Schedule
from .models import CreateContact
from django import forms


#Create the form class.
class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = CreateContact
        fields = '__all__'


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)


