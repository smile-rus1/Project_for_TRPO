from django.db.models import Count
from django.core.cache import cache
from .models import *

menu = [
    {"title": "События", "url_name": "events"},
    {"title": "Группы", "url_name": "groups"},
    {"title": "Обратная связь", "url_name": "contact"},
]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        groups = Groups.objects.all()
        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context["menu"] = user_menu
        context["group"] = groups

        return context
