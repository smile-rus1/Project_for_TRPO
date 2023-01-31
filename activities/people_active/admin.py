from django.contrib import admin
from .models import *
# Register your models here.


"""Настройка Админки"""


class ActivityAdmin(admin.ModelAdmin):
    """как будет отображаться в админке"""
    list_display = ("id", "title", 'create_date', "photo", "is_published")
    """как будут отображаться ссылки"""
    list_display_links = ("id", "title")
    """как будет искать по каким полям"""
    search_fields = ("title", "content")

    list_editable = ("is_published",)
    list_filter = ("is_published", "create_date")

    prepopulated_fields = {"slug": ("title",)}


class GroupsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)

    """
    указывает какое поле автоматически заполнять
    в данном случае заполняет slug на основе поля name
    """
    prepopulated_fields = {"slug": ("name",)}

"""Реализовать потом"""
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "message")
    search_fields = ("message",)
    prepopulated_fields = {"slug": ("message",)}


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(ActivityDiscussion)

# admin.site.register(ActivityDiscussion, DiscussionAdmin)
