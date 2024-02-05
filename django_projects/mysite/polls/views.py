from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
from .models import Person

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
    