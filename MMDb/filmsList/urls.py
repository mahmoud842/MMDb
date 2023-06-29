from django.urls import path
from . import views

app_name = "filmsList"
urlpatterns = [
     path("", views.index, name="index"),
     path("add", views.addFilm, name="add")
]
