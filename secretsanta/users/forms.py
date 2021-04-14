from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''
	This class inherits from and extends Django's default UserCreationForm,
	hence we import 'django.contrib.ath.forms import UserCreationForm' above.
	We can requires more fields when creating our own form that inherits from
	UserCreationForm.
'''
class UserRegisterForm(UserCreationForm):
	# Our own extra fields go here
	email = forms.EmailField()

	# This inner class lists all of the fields,
	# inlcuding the fields inherited from UserCreationForm
	class Meta:
		# Specifies the model that is being affected
		model = User 

		# The order in which the fields are listed in 'fields'
		# will affect the order they appear in the form.
		fields = ['username', 'email', 'password1', 'password2']

		