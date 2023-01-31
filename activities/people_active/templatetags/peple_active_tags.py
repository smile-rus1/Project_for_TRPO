""" файл для создания пользовательских тегов """

from django import template
from people_active.models import *

register = template.Library()


@register.simple_tag()
def get_active():
    return Activity.object.all()


@register.inclusion_tag("people_active/list_active.html")
def show_activities():
    events = Activity.object.all()
    return {"events": events}
