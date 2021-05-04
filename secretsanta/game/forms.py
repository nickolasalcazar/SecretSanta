from django import forms
from .models import Game, Player
from django.forms import formset_factory

class CreateGameForm(forms.ModelForm):

    title = forms.CharField()

    class Meta:
        model = Game
        fields = ['title']

class CreatePlayerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = Player
        fields = ['first_name', 'last_name']

CreatePlayerFormset = formset_factory(CreatePlayerForm, extra=2)
