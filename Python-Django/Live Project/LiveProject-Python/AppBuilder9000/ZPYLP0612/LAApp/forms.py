from django.forms import ModelForm
from .models import Author

#Create the form class.
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
