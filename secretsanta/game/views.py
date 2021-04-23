from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
)

from django.contrib.auth.decorators import login_required

from .forms import CreateGameForm, CreatePlayerForm

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
	if request.method == 'POST':
		game_form = CreateGameForm(request.POST)
		#player_form = CreatePlayerForm

		# if game_form.is_valid() and player_form.is_valid():
		if game_form.is_valid():
			game_form.instance.host = request.user

			game_form.save()
			#player_form.save()

			messages.success(request, 'New game created.')
	else:
		game_form = CreateGameForm()

	context = {
		'game_form': game_form,
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
