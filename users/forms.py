from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    email_or_username = forms.CharField(max_length=125)
    password = forms.CharField(max_length=125)
