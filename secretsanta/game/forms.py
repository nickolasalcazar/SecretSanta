from django import forms
from .models import Game

class CreateGameForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Game
        fields = ['title']

class CreatePlayerForm(forms.ModelForm):
    pass