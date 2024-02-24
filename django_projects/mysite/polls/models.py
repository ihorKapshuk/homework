from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Notes(models.Model):
    note_name = models.CharField(max_length=100)
    note_text = models.CharField(max_length=200)
    note_category = models.CharField(max_length=100)
    note_user_name = models.CharField(max_length=150, default="name")