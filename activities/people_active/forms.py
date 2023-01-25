from django import forms
from .models import *


class UserForms(forms.Form):
    name = forms.CharField(label="Имя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    password_second = forms.CharField(label="Повтор пароля" ,widget=forms.PasswordInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Email")

    class Meta:
        model = Activity
        fields = ("name", "password", "password_second", "email")