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
	#first_name = models.CharField(max_length=25, default="")
	first_name = models.CharField(max_length=25, default="", blank=True)

	last_name = models.CharField(max_length=25, default="", blank=True)
	#last_name = models.CharField(max_length=25, blank=True)

	email = models.EmailField(max_length=254, null=True, default='', blank=True)

	# The recipient of the Player, to whome the Player is assigned to gift.
	# Can be null. Will be set to null if the recipient is deleted.
	recipient = models.OneToOneField('self', null=True, on_delete=models.SET_NULL) 

	def __str__(self):
		return f'Player {self.first_name} {self.last_name}'

	def save(self, *args, **kwargs):
		# if first_name is empty, delete the whole objects
		# problema:
		#	-	if user leaves first_name blank, player gets deleted
		#		even though last_name and email are filled in
		#			Solution: - turn first_name and last_name into one 'name' field
		#					  - if 'name' field is blank, then delete
		#					  - JS: for all Player Form rows:
		#								if 'email' field is filled and 'name' is not
		#									display requirement next to field
		if not self.first_name:
			self.delete()
		# else save as normal
		else:
			super(Player, self).save(*args, **kwargs)