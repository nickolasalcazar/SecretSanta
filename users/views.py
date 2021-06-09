from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm #ProfileUpdateForm

from django.contrib.auth.decorators import login_required

'''
    Registration page
'''
def register(request):
    # If user is already logged in, redirect to homepage
    if request.user.is_authenticated: return redirect('/')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account as been created, {username}.')

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

'''
    View personal profile page
'''
@login_required
def profile(request):
    # If we get a POST request, create forms
    if request.method == 'POST':
        # Passing 'instance=request.user' will pre-populate the form
        #   with the User's existing information.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            #p_form.save()

            messages.success(request, 'Account has been updated.')
            return redirect('profile') # Reload the page
    else:
        # Else create forms that do not pass data
        u_form = UserUpdateForm(instance=request.user)
        #p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        #'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
