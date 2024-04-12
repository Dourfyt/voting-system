from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from golos.models import UserD

class UserAuth(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "example@example.com"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
    }))
    class Meta:
        model = UserD
        fields = ("username","password")