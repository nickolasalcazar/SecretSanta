from django import forms
from .models import Game, Player
from django.forms import formset_factory, inlineformset_factory

class CreateGameForm(forms.ModelForm):

    title = forms.CharField()

    class Meta:
        model = Game
        fields = ['title']

class CreatePlayerForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'optional'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'optional'}))

    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email']

# Can the 'extra' variable be changed dynamically?
CreatePlayerFormset = formset_factory(CreatePlayerForm, extra=4) # max_forms = 32

'''
	Inline formset for set of Player forms.
	Defining PlayerInlineFormSet in forms.py prevents having to import 'django.forms'
	to views.py.
	Used in the game.views.updateGame
'''
PlayerInlineFormSet = inlineformset_factory(Game, Player,
                            fields=('first_name', 'last_name', 'email'),
                            widgets={
                                'last_name': forms.TextInput(attrs={'placeholder': 'optional'}),
                                'email': forms.TextInput(attrs={'placeholder': 'optional'})
                                })