# chat/urls.py
from django.urls import path

from .views import *
from django.contrib.auth import views

app_name = "chat"

urlpatterns = [
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),
]