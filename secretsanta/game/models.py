from django.db import models
from django.contrib.auth.models import User

'''
	The Host of a Game is a User object. A User object is the foreign key of a Game.
'''
class Game(models.Model):
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=25, default="Untitled Game")

'''
	The Game object is a foreign key of Player objects.
'''
class Player(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=25, default="First name")
	last_name = models.CharField(max_length=25, default="Last name")
	#last_name = models.CharField(max_length=25, blank=True)
