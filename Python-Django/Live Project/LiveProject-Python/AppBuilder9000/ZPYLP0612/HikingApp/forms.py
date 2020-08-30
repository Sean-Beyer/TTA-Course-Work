from django import forms
from django.forms import ModelForm
from .models import Hikes
import datetime


class HikeForm(ModelForm):
    class Meta:
        model = Hikes
        fields = ('Hike_Name', 'Date', 'Start_Time', 'Difficulty', 'Completed', 'End_Time', 'Rating')
        widgets = {

            'Date':  forms.DateInput(attrs={'type': 'date'}),
            'Start_Time': forms.TimeInput(attrs={'type': 'time'}),
            'End_Time':  forms.TimeInput(attrs={'type': 'time'}),
            'Hike_Name':  forms.TextInput(attrs={'placeholder':'Enter Hike\'s Name'}),
        }


