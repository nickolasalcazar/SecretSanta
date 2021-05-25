from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.contrib.auth.decorators import login_required

from .forms import (
    CreateGameForm,
    CreatePlayerFormset,
    PlayerInlineFormSet
)

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.models import User
from .models import Game, Player

from django.forms.models import inlineformset_factory

from django.urls import reverse

import random
import secrets

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
        if game_form.is_valid() and player_formset.is_valid():
            # Assign curent user as host of Game
            game_form.instance.host = request.user
            game_form.save()

            # Handle forms for creating Player objects
            # Extract names from form and save
            for form in player_formset:
                name = form.cleaned_data.get('name')
                # if name is empty, do not save Player
                if name == '' or name == None: continue
                email = form.cleaned_data.get('email')
                Player(game=game_form.instance, name=name, email=email).save()

            messages.success(request, 'New game created.')

            assignPairs(game_form.instance)

            return redirect('game-detail', game_form.instance.id)
    else:
        game_form = CreateGameForm()

    context = {
        'game_form': game_form,
        'player_formset': player_formset,
        'action_title': 'Create'
    }

    return render(request, 'game/game_form.html', context)

'''
    Function-based view for updating games.
    Passed the game_pk of the game to be updated.
'''
def updateGame(request, pk):
    game = Game.objects.get(pk=pk)
    # If User is not host of game, redirect them to homepage
    if request.user != game.host: return redirect('game-home')
    
    players = game.player_set.all()

    if request.method == 'POST':
        game_form = CreateGameForm(request.POST, instance=game)
                                                            # is request.FILES needed?
        player_formset = PlayerInlineFormSet(request.POST, request.FILES, instance=game)

        #if game_form.is_valid() and player_formset.is_valid():
        if game_form.is_valid():
            if player_formset.is_valid():
                player_formset.save()

            game_form.save()
            messages.success(request, 'Game updated.')

            # Before submitting an update to Game the Host should be
            # notifed that updating will cause Players to be reassigned.
            assignPairs(game_form.instance)

            #return redirect('game-home')
            return redirect('game-detail', pk)
    else:
        game_form = CreateGameForm(instance=game)
        #player_formset = CreatePlayerFormset()
        player_formset = PlayerInlineFormSet(instance=game)

    context = {
        'game_form': game_form,
        'player_formset': player_formset,
        'action_title': 'Update'
    }

    return render(request, 'game/game_form.html', context)

'''
    Function-based view for displaying the list of Games created by a User.
'''
def gameListView(request, pk):
    host = User.objects.get(pk=pk)
    # If User is not host of game, redirect them to homepage
    if request.user != host: return redirect('game-home')

    games = Game.objects.filter(host=host)

    context = {
        'games': games
    }
    return render(request, 'game/view_games.html', context)

class GameDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Game
    # For UserPassesTestMixin: is the request.user the game.host?
    def test_func(self):
        game = self.get_object()
        return self.request.user == game.host

# Add LoginRequiredMixin
class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'game/confirm_delete_game.html'
    model = Game

    def get_success_url(self):
        host = self.object.host 
        return reverse( 'view-games', kwargs={'pk': host.id})

    '''
        Overriding the form_valid() method.
        This function sets the author of the post to the user who posts it.
        This must be specified, otherwise the author of the post will be NULL,
        and that will throw an error.
    '''
    def form_valid(self, form):
        form.instance.host = self.request.user # Set author = user
        return super().form_valid(form)

    # For UserPassesTestMixin: is the request.user the game.host?
    def test_func(self):
        game = self.get_object()
        return self.request.user == game.host

'''
    Randomly assigns each Player a distinct recipient.
    Performance is contingent on game having an even number of Players.
    Throws an exception if game has odd number of Players.
'''
def assignPairs(game):
    players = game.player_set.all()
    print('assignPairs() for player_set: ', players)
    print('             players.count(): ', players.count())
    print('                len(players): ', len(players))


    if players.count() % 2 != 0: raise Exception('Odd number of players.')

    unassigned_players = list(game.player_set.all())

    # Unassign all recipients
    players.update(recipient=None)


    # Still has a chance of infinite loop

    # Re-assign all recipients
    for player in players:
        # Keep generating an index until a self-assignment is avoided
        z = 0
        
        choice = None

        while (True):
            z += 1
            if (z > 10): raise Exception('Infinite loop')


            #i = random.randint(0, len(unassigned_players)-1)
            choice = secrets.choice(unassigned_players)

            print(player.name, '->', choice.name, '?')

            if (player != choice): break

            print('\tlooping')


        print('\t', player.name, '->', choice.name, '\b')
        


        player.recipient = choice
        unassigned_players.remove(choice)

        print('\t', unassigned_players)

        player.save()








