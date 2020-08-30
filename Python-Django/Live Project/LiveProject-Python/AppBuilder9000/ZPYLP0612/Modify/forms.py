from django.forms import ModelForm
from .models import MNews

#Create the form class.
class MNewsForm(ModelForm):
    class Meta:
        model = MNews
        fields = '__all__'