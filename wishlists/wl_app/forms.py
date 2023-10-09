from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput, PasswordInput


User = get_user_model()

class WishlistForm(forms.Form):
    wishlist = forms.CharField(max_length=150,
        widget=TextInput(attrs={
            'class': 'form-control text-center col-auto mb-3',
            'type': 'text',
            'placeholder': 'Название списка'
            }),
    )

class WishForm(forms.Form):
    wish = forms.CharField(required=True, max_length=100)
    link = forms.URLField(required=False)
    price = forms.FloatField(min_value=0, max_value=999999, required=False)

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={
            'class': 'form-control col-auto mb-3',
            'type': 'text',
            'placeholder': 'Имя пользователя',
            }),
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control col-auto mb-3',
            'type': 'password',
            'placeholder': 'Пароль',
            }),
        )

class RegisterUser(UserCreationForm):
    password1 = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control col-auto mb-3',
            'type': 'password',
            'placeholder': 'Пароль'
            }),
    )
    password2 = forms.CharField(
        widget=PasswordInput(attrs={
            'class': 'form-control col-auto mb-3',
            'type': 'password',
            'placeholder': 'Повторите пароль'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
            'class': 'form-control col-auto mb-3',
                'placeholder': 'Имя пользователя'
                }),
        }
