from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Profile

'''
    This class inherits from and extends Django's default UserCreationForm,
    hence we import 'django.contrib.ath.forms import UserCreationForm' above.
    We can requires more fields when creating our own form that inherits from
    UserCreationForm.
'''
class UserRegisterForm(UserCreationForm):
    # Our own extra fields go here
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    # This inner class lists all of the fields,
    # inlcuding the fields inherited from UserCreationForm
    class Meta:
        # Specifies the model that is being affected
        model = User 

        # The order in which the fields are listed in 'fields'
        # will affect the order they appear in the form.
        fields = ['username', 'email',
                    'first_name', 'last_name', 
                    'password1', 'password2']

'''
    This form is created for allowing users to update their own profiles,
    such as their 'username' and 'email'.
    It must inherit from form.ModelForm.
    It has all of the same fields as UserRegisterForm, excluding passwords.
'''
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


'''
    This form is for allowing users to update their profile image.
'''
'''
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        #fields = ['image']
'''
