from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput


class WishlistForm(forms.Form):
    wishlist = forms.CharField(max_length=150)

class WishForm(forms.Form):
    wish = forms.CharField(required=True, max_length=100)
    link = forms.URLField(required=False)
    price = forms.FloatField(min_value=0, max_value=99999, required=False)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterUser(UserCreationForm):
    pass

