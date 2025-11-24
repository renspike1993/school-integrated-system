from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
        })
    )
