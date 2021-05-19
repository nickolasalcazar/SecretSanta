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
    UpdateView,
    DeleteView
)

from .models import Game, Player

from django.forms.models import inlineformset_factory

import random

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
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')

                # Save Player instance
                if first_name:
                    Player(game=game_form.instance,
                        first_name=first_name, last_name=last_name).save()

            messages.success(request, 'New game created.')

            assignPairs(game_form.instance) ############################ TESTING

            return redirect('game-home')
    else:
        game_form = CreateGameForm()

    context = {
        'game_form': game_form,
        'player_formset': player_formset,
        'action_title': 'Create'
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

    PlayerInlineFormSet = inlineformset_factory(Game, Player, fields=('first_name', 'last_name'))

    if request.method == 'POST':
        game_form = CreateGameForm(request.POST, instance=game)
        player_formset = PlayerInlineFormSet(request.POST, request.FILES, instance=game)

        #if game_form.is_valid() and player_formset.is_valid():
        if game_form.is_valid():


            if player_formset.is_valid():
                player_formset.save()

            game_form.save()
            messages.success(request, 'Game updated.')

            # Before submitting an update to Game the Host should be
            # notifed that updating will cause Players to be reassigned.
            assignPairs(game_form.instance) ############################ TESTING

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

# Add LoginRequiredMixin
class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'game/confirm_delete_game.html'
    model = Game
    success_url = '/game/view-games'

    '''
        Overriding the form_valid() method.
        This function sets the author of the post to the user who posts it.
        This must be specified, otherwise the author of the post will be NULL,
        and that will throw an error.
    '''
    def form_valid(self, form):
        form.instance.host = self.request.user # Set author = user
        return super().form_valid(form)

    '''
        Checks if the user who is updating the post is the author of the post.
        (Only authors can edit their own posts. This prevents anyone from editing
        anyone else's post.)

        If a non-author attempts to edit a post, they will be returned a 403 Forbidden page.
    '''
    def test_func(self):
        game = self.get_object()
        return self.request.user == game.host

'''
    Randomly assigns each Player a distinct recipient.
'''
def assignPairs(game):
    players = game.player_set.all()
    unassigned_players = list(game.player_set.all())

    # Query Player object by id
    # Player.objects.get(pk=player.id)

    for player in players:
        i = random.randint(0, len(unassigned_players)-1)

        print('index = ', i, ', len = ', len(unassigned_players))

        #print('unassigned_players[i]', unassigned_players[i])
        #print('\tAssigning ', player.first_name, ' to ', unassigned_players[i].first_name)
        
        player.recipient = unassigned_players[i]
        
        unassigned_players.remove(unassigned_players[i])
        player.save()











