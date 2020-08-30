from django.forms import ModelForm
from .models import ShoeClosetModel


# Create the form class.
class ShoeClosetForm(ModelForm):
    class Meta:
        model = ShoeClosetModel
        fields = '__all__'
