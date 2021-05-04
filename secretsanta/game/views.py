from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.contrib.auth.decorators import login_required

from .forms import (
    CreateGameForm,
    CreatePlayerFormset
)

# The following import will no longer be needed after CreateGameForm and CreatePlayerForm
# classes are implemented.
from django.views.generic import CreateView

from .models import Game, Player

'''
    Function-based view for the home page of the site.
'''
def home(request):
    context = { }
    return render(request, 'game/home.html', context)

'''
    Handles creation of new Game object.
'''
@login_required
def createGame(request):
    game_form = CreateGameForm(request.POST or None)
    player_formset = CreatePlayerFormset(request.POST or None)

    if request.method == 'POST':

        # if game_form.is_valid() and player_form.is_valid():
        if game_form.is_valid() and player_formset.is_valid():
            # Assign curent user as host of Game
            game_form.instance.host = request.user
            # Save the game
            game_form.save()

            # Handle forms for creating Player objects
            # Extract names from form and save
            for form in player_formset:
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')

                # Save Player instance
                if first_name:
                    Player(game=game_form.instance, first_name=first_name, last_name=last_name).save()


            #player_form.save()

            messages.success(request, 'New game created.')

            return redirect('game-home')
    else:
        game_form = CreateGameForm()
        #player_formset = CreatePlayerFormset()

    context = {
        'game_form': game_form,
        'player_formset': player_formset,
    }

    return render(request, 'game/game_form.html', context)


'''
class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game # The model that will be created
    fields = ['date']
    
    ''
        Overriding the form_valid() method.
        This function sets the author of the post to the user who posts it.
        This must be specified, otherwise the author of the post will be NULL,
        and that will throw an error.
    ''
    def form_valid(self, form):
        form.instance.author = self.request.user # Set author = user
        return super().form_valid(form)
'''
