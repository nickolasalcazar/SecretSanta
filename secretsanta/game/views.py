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

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView
)

from .models import Game, Player

from django.forms.models import inlineformset_factory # For InlineFormSet ###############

'''
    Function-based view for the home page of the site.
'''
def home(request):
    context = { }
    return render(request, 'game/home.html', context)

'''
    Handles creation of new Game object using a function-based view.
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

# Note: implement login-required -- add parameter LoginRequiredMixin
class GameListView(ListView):
    model = Game
    template_name = 'game/view_games.html'
    context_object_name = 'games'

# Note: implement login-required -- add parameter LoginRequiredMixin
class GameDetailView(DetailView):
    model = Game

'''
    Function-based view for updating games.
    Passed the game_pk of the game to be updated.
'''
def updateGame(request, pk):
    game = Game.objects.get(pk=pk)
    players = game.player_set.all()

    #game_form = CreateGameForm(request.POST or None)
    #game_form = CreateGameForm(instance=game)

    PlayerInlineFormSet = inlineformset_factory(Game, Player, fields=('first_name', 'last_name'))

    print('A')
    if request.method == 'POST':
        print('B')

        game_form = CreateGameForm(request.POST, instance=game)
        player_formset = PlayerInlineFormSet(request.POST, request.FILES, instance=game)

        print(player_formset.errors)

        #if game_form.is_valid() and player_formset.is_valid():
        if game_form.is_valid():
            print('C')

            player_formset.save()
            
            game_form.save()

            messages.success(request, 'Game updated.')
            return redirect('game-home')
    else:
        game_form = CreateGameForm(instance=game)
        #player_formset = CreatePlayerFormset()
        player_formset = PlayerInlineFormSet(instance=game)

    context = {
        'game_form': game_form,
        'player_formset': player_formset,
    }

    return render(request, 'game/game_form.html', context)



















