from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Login", widget=forms.TextInput(attrs={"class": "forms-input"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "forms-input"})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
