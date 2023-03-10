from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("events/", Events.as_view(), name="events"),
    path("addpage/", AddPage.as_view(), name="add_page"),
    path("groups/", ShowGroup.as_view(), name="groups"),
    path("login/", LoginUser.as_view(), name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("contact/", contact, name="contact"),
    path("logout/", logout_user, name="logout"),
    path("discussion/", Discussion.as_view(), name="discussion"),
    path("discussion_add/", discussion_add, name="discussion_add"),
    path("subscribe/", subscribe, name="subscribe"),
    path("unsubscribe/", unsubscribe, name="unsubscribe"),
    path("add_group/", AddGroup.as_view(), name="add_group"),
    path("profile/", profile, name="profile"),
    path("help_system", help_system, name="help_system"),

    path("post/<slug:post_slug>/", ShowPostInfo.as_view(), name="post"),
    path("groups/<slug:group_slug>/", ShowAboutGroup.as_view(), name="show_group"), # информация внутри группы


]
