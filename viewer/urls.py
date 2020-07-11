from django.urls import path
from . import views


urlpatterns = [
    path("<str:entryname>", views.index, name="Doc"),
    path("edit/<str:name>", views.edit, name="edit")
]