from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, NoteForm
from .models import Person, Notes
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "main.html")

def return_child_one(request):
    users_data = Person.objects.all().values()
    return render(request, "child.html", context={"users_data" : users_data})

def my_form(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            my_obj = Person()
            first_name = form.cleaned_data["first_name"]
            my_obj.first_name = first_name
            last_name = form.cleaned_data["second_name"]
            my_obj.last_name = last_name
            my_obj.save()
    else:
        form = NameForm()
    return render(request, "form.html", {"form" : form})

@login_required
def my_notes_form(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            my_obj = Notes()
            note_name = form.cleaned_data["note_name"]
            my_obj.note_name = note_name
            note_text = form.cleaned_data["note_text"]
            my_obj.note_text = note_text
            note_category = form.cleaned_data["note_category"]
            my_obj.note_category = note_category
            
            cur_user = request.user
            my_obj.note_user_name = cur_user.username
            my_obj.save()
            return HttpResponseRedirect("/polls/notes/")
    else:
        form = NoteForm()
    return render(request, "notes_form.html", context={"form" : form})

def my_notes(request):
    users_data = Notes.objects.all().order_by("-id").values()
    return render(request, "notes.html", context={"notes" : users_data})

@login_required
def my_notes_update(request, id):
    obj = Notes.objects.get(id=id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note_name = form.cleaned_data["note_name"]
            obj.note_name = note_name
            note_text = form.cleaned_data["note_text"]
            obj.note_text = note_text
            note_category = form.cleaned_data["note_category"]
            obj.note_category = note_category

            cur_user = request.user
            obj.note_user_name = cur_user.username
            obj.save()
            return HttpResponseRedirect("/polls/notes/")
    else:
        form = NoteForm()
    return render(request, "notes_update.html", context={"form" : form})

def my_notes_del(request, id):
    obj = Notes.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/polls/notes/")
    return render(request, "notes_del.html", context={"obj" : obj})