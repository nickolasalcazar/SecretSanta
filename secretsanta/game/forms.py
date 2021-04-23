from django import forms
from .models import Game

class CreateGameForm(forms.ModelForm):
    title = forms.CharField()
    #date = forms.DateField()

    class Meta:
        model = Game
        fields = ['title', ] #'date']

class CreatePlayerForm(forms.ModelForm):
    pass