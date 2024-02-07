from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)

class BookForm(forms.Form):
    name = forms.CharField(max_length=30)
    author = forms.CharField(max_length=30)
    year = forms.IntegerField()