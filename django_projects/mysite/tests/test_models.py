from django.test import TestCase
from polls.models import Person, Notes

class PersonTestCase(TestCase):

    def setUp(self):
        Person.objects.create(first_name="Name1", last_name="Surename1")
        Person.objects.create(first_name="Name2", last_name="Surename2")

    def test_creation(self):
        person1 = Person.objects.get(first_name="Name1")
        person2 = Person.objects.get(first_name="Name2")
        self.assertEqual(person1.last_name, "Surename1")
        self.assertEqual(person2.last_name, "Surename2")

class NotesTestCase(TestCase):

    def setUp(self):
        Notes.objects.create(note_name="Test note", note_text="Text", note_category="General", note_user_name="Tester")
        Notes.objects.create(note_name="Test note2", note_text="Text2", note_category="General2", note_user_name="Tester2")
    
    def test_creation(self):
        note1 = Notes.objects.get(note_name="Test note")
        note2 = Notes.objects.get(note_name="Test note2")
        self.assertEqual(note1.note_text, "Text")
        self.assertEqual(note2.note_text, "Text2")
        self.assertEqual(note1.note_category, "General")
        self.assertEqual(note2.note_category, "General2")
        self.assertEqual(note1.note_user_name, "Tester")
        self.assertEqual(note2.note_user_name, "Tester2")