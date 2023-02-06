from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from .models import *
from .utils import *


"""
Форма для добавления событий!
"""


class AddEvents(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["title", "slug", "content", "photo", "is_published", "group"]

        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 30:
            raise ValidationError("Название поста не может быть больше 30 слов")

        return title

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) > 200:
            raise ValidationError("Вы привысили количество слов (MAX 200)")

        return content


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Введите пароль", widget=forms.TextInput(attrs={"class": "form-input"}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={"class": "form-input"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Введите пароль", widget=forms.TextInput(attrs={"class": "form-input"}))


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = DiscussionActive
        fields = ["message"]

        widgets = {
            "message": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }

    def clean_message(self):
        message = self.cleaned_data["message"]
        if len(message) > 500:
            raise ValidationError("Максимум 500 символов")

        return message



