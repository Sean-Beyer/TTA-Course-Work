from django.forms import ModelForm
from .models import Photography

#Create the form class.
class photographyform(ModelForm):
    class Meta:
        model = Photography
        fields = '__all__'