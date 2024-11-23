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


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_naem': 'First Name',
            'last_name': 'Last Name',
        }

        def clean_password2(self):
            cd = self.clean_field
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match')
            return cd['password']
            

        def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('E-mail is exists')
            return email