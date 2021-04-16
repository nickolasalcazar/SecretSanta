from django.shortcuts import render
from django.utils import timezone

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
)

from django.views.generic import (
	CreateView
)

from .models import Game, Player

'''
    Function-based view for the home page of the site.
'''
def home(request):
    context = { }
    return render(request, 'game/home.html', context)



class GameCreateView(LoginRequiredMixin, CreateView):
	model = Game # The model that will be created
	fields = ['date']
	
	'''
		Overriding the form_valid() method.
		This function sets the author of the post to the user who posts it.
		This must be specified, otherwise the author of the post will be NULL,
		and that will throw an error.
	'''
	def form_valid(self, form):
		form.instance.author = self.request.user # Set author = user
		return super().form_valid(form)
