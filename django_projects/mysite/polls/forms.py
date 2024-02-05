from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)