from django.forms import ModelForm
from .models import Game
from django import forms

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

GAME_TYPES = [
    ('boardgame', "Board Games"),
    ('rpg', 'RPGs'),
]

class SearchForm(forms.Form):
    game_type = forms.CharField(widget=forms.Select(choices=GAME_TYPES))