from django import forms
from .models import *


"""
Форма для добавления событий!
"""
class AddEvents(forms.Form):
    title = forms.CharField(max_length=255, label="Название", widget=forms.TextInput(attrs={"class": "form-input"}))
    slug = forms.SlugField(max_length=255, label="Slug", widget=forms.TextInput(attrs={"class": "form-input"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 60, "rows": 10}), label="Текст события",
                              )
    is_published = forms.BooleanField(label="Публикация", required=False, initial=True,
                                      )
    group = forms.ModelChoiceField(queryset=Groups.objects.all(), label="К какой группе принадлежит",
                                   required=False, empty_label="Группы нет",
                                   widget=forms.TextInput(attrs={"class": "form-input"}))

