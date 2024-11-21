from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(
        label="Login", widget=forms.TextInput(attrs={"class": "forms-input"})
    )
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "forms-input"})
    )
