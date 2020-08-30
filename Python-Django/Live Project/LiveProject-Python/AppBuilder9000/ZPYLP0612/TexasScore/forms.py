from django.forms import ModelForm
from .models import TexasGame


# Create the form class.
class TexasForm(ModelForm):
    class Meta:
        model = TexasGame
        fields = '__all__'
