from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		# Create a UserCreationForm with the data from the POST request
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')

			# Flash success message
			# messages.success(request, f'Account created for {username}!')
			messages.success(request, 'Your account as been created, you may now log in')

			# Redirect user to homepage
			return redirect('login')
	else:
		# Else create an empty form
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

