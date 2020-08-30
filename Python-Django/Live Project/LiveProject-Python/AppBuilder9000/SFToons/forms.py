from django.forms import ModelForm
from .models import Character
from .models import Items

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'


# class srdForm(ModelForm):
#     class Meta:
#         model = Items
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['item'].queryset = Items.objects.none()