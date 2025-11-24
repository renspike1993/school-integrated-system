from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Enter your username",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Enter your password",
            }
        ),
    )
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300",
        "placeholder": "Enter your email"
    }))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Enter your username"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Enter password"
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300",
                "placeholder": "Confirm password"
            }),
        }