from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("child/", views.return_child_one, name="child"),
    path("form/", views.my_form, name="form")
]