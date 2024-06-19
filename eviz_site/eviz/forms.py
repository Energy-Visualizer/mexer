from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import EvizUser

class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'joe@gmail.com'})
    )
    institution = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "e.g. Calvin University"})
    )
    country = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "e.g. United States"})
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = EvizUser 
        fields = ['username', 'email', 'password1', 'password2', 'institution', 'country']

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )