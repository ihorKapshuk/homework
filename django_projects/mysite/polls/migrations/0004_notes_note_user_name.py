# Generated by Django 5.0.1 on 2024-02-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_notes_delete_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note_user_name',
            field=models.CharField(default='name', max_length=100),
        ),
    ]