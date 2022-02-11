from django import forms
from django.forms import Form


class LoginForm(Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput
    )
