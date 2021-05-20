from django.db import models
from django.contrib.auth.models import User

'''
	The Host of a Game is a User object. A User object is the foreign key of a Game.
'''
class Game(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=25, default="Untitled Game")

	def __str__(self):
		return f'Game "{self.title}"'

'''
	The Game object is a foreign key of Player objects.
'''
class Player(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=25, default="")
	last_name = models.CharField(max_length=25, default="", blank=True)
	#last_name = models.CharField(max_length=25, blank=True)

	email = models.EmailField(max_length=254, null=True, default='', blank=True)

	# The recipient of the Player, to whome the Player is assigned to gift.
	# Can be null. Will be set to null if the recipient is deleted.
	recipient = models.OneToOneField('self', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f'Player {self.first_name} {self.last_name}'


