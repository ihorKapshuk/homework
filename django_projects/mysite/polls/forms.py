from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    second_name = forms.CharField(max_length=30)

class NoteForm(forms.Form):
    note_name = forms.CharField(label="Назва нотатки", max_length=100)
    note_text = forms.CharField(label="Текст нотатки",max_length=200)
    note_category = forms.CharField(label="Категрія нотатки",max_length=100)