from django import forms
from django.contrib.auth.models import User

from app.models import AppUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('picture',)