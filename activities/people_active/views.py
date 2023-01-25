from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, \
    FormView
# Create your views here.
from .models import *
# from .utils import *
from .forms import *


menu = [
    {"title": "События", "url_name": "events"},
    {"title": "Добавить статью событий", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},

    {"title": "Войти", "url_name": "login"},
]


def index(request):
    active = Activity.objects.all()
    context = {
        "active": active,
        "menu": menu,
        "title": "Главная страница"
    }

    return render(request, "index.html", context=context)


def addpage(request):
    return HttpResponse("addasdasdapage")


def show_post(request, post_id):
    return HttpResponse(f"Пост {post_id}")


def events(request):
    return render(request, "Events.html")


def group(request):
    group = Groups.objects.all()
    context = {
        "group": group,
        "menu": menu,
        "title": "События"
    }
    return render(request, "Group.html", context=context)


def contact(request):
    return render(request, "Contact.html")


def login(request):
    return HttpResponse("asdasdads")

def pageNotFound(request, exeption):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")




