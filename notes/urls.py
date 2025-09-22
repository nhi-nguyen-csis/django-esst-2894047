from django.urls import path
from notes.views import list

urlpatterns = [path("notes", list, name="list"),]