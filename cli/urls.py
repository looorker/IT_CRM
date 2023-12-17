from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("analitics/", views.analisus, name="analisus"),
    path("send/", views.send, name="send"),
    path("manage/", views.manage, name="manage"),
    path("register/", views.register, name="register"),
    path("users/", views.UserListView.as_view(), name="users"),
    path("analitics/", views.download, name="download_e"),
    path("users/<int:pk>", views.UserView.as_view(), name="user_card"),
    path("users/<int:pk>/edit/", views.UserUpdateView.as_view(), name="user_edit"),
    path("users/<int:pk>/delete/", views.UserDeliteView.as_view(), name="user_del"),
    path("users/seacrh/", views.UserSearchView.as_view(), name="users_q"),
    path("event_add/", views.MeetupAdd.as_view(), name="event_add"),
    path('<int:pk>/', views.MeetupView.as_view(), name="mt_card"),
    path('<int:pk>/edit/', views.MeetupUpdateView.as_view(), name="mt_edit"),
    path('<int:pk>/delete/', views.MeetupDeliteView.as_view(), name="mt_del"),

]