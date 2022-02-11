from django import forms
from django.forms import Form


class RegisterForm(Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) > 100:
            self.add_error('email', 'L\'email est trop longue')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            self.add_error('password', 'Le mot de passe est trop court')
        if len(password) > 100:
            self.add_error('password', 'Le mot de passe est trop long')

        return password