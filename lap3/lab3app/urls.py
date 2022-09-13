from django.urls import path
from . import views

app_name = "lab3app"

urlpatterns = [
path("", views.welcome, name="home"),
path("today/", views.day, name="today"),
path("books/", views.book, name="books"),
path("pass/", views.pas_w, name="pass"),
path("contact/", views.contact , name="contact"),
]
