from django.forms import ModelForm
from .models import Comedies

# Create a form for Comedies model
class ComedyForm(ModelForm):
    class Meta:
        model = Comedies
        fields = '__all__'







