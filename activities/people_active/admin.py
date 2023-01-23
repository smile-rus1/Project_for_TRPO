from django.contrib import admin
from .models import *
# Register your models here.


"""Настройка Админки"""


class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(Activity, ActivityAdmin)

