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
	name = models.CharField(max_length=45, default='', blank=True)
	#first_name = models.CharField(max_length=25, default="", blank=True)
	#last_name = models.CharField(max_length=25, default="", blank=True)
	email = models.EmailField(max_length=254, null=True, default='', blank=True)

	# The recipient of the Player is to whome the Player is assigned to gift.
	# Can be null. Will be set to null if the recipient is deleted.
	recipient = models.OneToOneField('self', null=True, on_delete=models.SET_NULL) 

	def __str__(self):
		#return f'Player {self.first_name} {self.last_name}'
		return f'Player {self.name}'

	def save(self, *args, **kwargs):
		# problem:
		#	-	if user leaves first_name blank, player gets deleted
		#		even though last_name and email are filled in
		#			Solution: - turn first_name and last_name into one 'name' field
		#					  - if 'name' field is blank, then delete
		#					  - JS: for all Player Form rows:
		#								if 'email' field is filled and 'name' is not
		#									display requirement next to field
		

		# if name is empty, delete the Player
		if not self.name:
			self.delete()
		# else save as normal
		else:
			super(Player, self).save(*args, **kwargs)

games_count = Game.objects.count()

player_count_avg = round(Player.objects.count() / games_count, 1)




