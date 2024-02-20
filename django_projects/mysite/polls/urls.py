from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("child/", views.return_child_one, name="child"),
    path("form/", views.my_form, name="form"),
    path("notes/", views.my_notes, name="notes"),
    path("notes_form/", views.my_notes_form, name="notes_form"),
    path("notes_update/<int:id>/", views.my_notes_update, name="notes_update"),
    path("notes_del/<int:id>/", views.my_notes_del, name="notes_del"),
]