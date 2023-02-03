from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, \
    FormView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from .utils import *
from .forms import *


class ShowGroup(DataMixin, ListView):
    model = Groups
    template_name = "Group.html"
    context_object_name = "group"
    allow_empty = False

    def get_queryset(self):
        return Activity.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Все группы")

        return context | data_mixin_def


class HomePage(DataMixin, ListView):
    model = Activity
    template_name = "index.html"
    context_object_name = "active"

    """Передаем контекст из меню"""
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Главная страница")

        return context | data_mixin_def


class Events(DataMixin, ListView):
    model = Activity
    template_name = "Events.html"
    context_object_name = "active"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="События")

        return context | data_mixin_def

    def get_queryset(self):
        return Activity.objects.filter(is_published=True)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    """берем с forms.py"""
    form_class = AddEvents
    template_name = "add_events.html"
    success_url = reverse_lazy("events")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Добавление в ленту событий")

        return context | data_mixin_def


class ShowAboutGroup(DataMixin, DetailView):
    model = Groups
    template_name = "show_group_info.html"
    context_object_name = "show"
    slug_url_kwarg = "group_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Информация о группе")

        return context | data_mixin_def


class ShowPostInfo(DataMixin, DetailView):
    model = Activity
    template_name = "show_post_events.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Информация о событии")

        return context | data_mixin_def


def contact(request):
    context = {
        "menu": menu,
        "title": "Контакты"
    }
    return render(request, "Contact.html", context=context)


def pageNotFound(request, exeption):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class DiscussionADD(DataMixin, CreateView):
    form_class = DiscussionForm
    template_name = "discussion_add.html"
    success_url = reverse_lazy("discussion")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Написать сообщение")

        return context | data_mixin_def

    def form_valid(self, form):
        user = form.save()
        return redirect("discussion")


class Discussion(DataMixin, ListView):
    model = DiscussionActive
    template_name = "discussion.html"
    context_object_name = "discussion"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Обсуждение")

        return context | data_mixin_def


class RegisterUser(DataMixin, CreateView):
    template_name = "register_user.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Регистрация")

        return context | data_mixin_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("events")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_mixin_def = self.get_user_context(title="Авторизация")

        return context | data_mixin_def

    def get_success_url(self):
        return reverse_lazy("events")


def logout_user(request):
    logout(request)
    return redirect("home")
