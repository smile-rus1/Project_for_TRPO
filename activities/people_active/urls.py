from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("events/", events, name="events"),
    path("addpage/", addpage, name="add_page"),
    path("groups/", group, name="groups"),
    path("login/", login, name="login"),
    path("contact/", contact, name="contact"),
    path("post/<int:post_id>/", show_post, name="post"),
    path("groups/<int:group_id>/", show_group, name="show_group")


]
