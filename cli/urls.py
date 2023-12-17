from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("analitics/", views.analisus, name="analisus"),
    path("send/", views.send, name="send"),
    path("manage/", views.manage, name="manage"),
    path("register/", views.register, name="register"),
    path("event_add/", views.event_add, name="event_add"),
    path('<int:pk>/', views.MeetupView.as_view(), name="mt_card"),
    path('<int:pk>/edit/', views.MeetupUpdateView.as_view(), name="mt_edit"),

]