from django.test import TestCase
from polls.models import Person

class PersonTestCase(TestCase):

    def setUp(self):
        Person.objects.create(first_name="Name1", last_name="Surename1")
        Person.objects.create(first_name="Name2", last_name="Surename2")

    def test_creation(self):
        person1 = Person.objects.get(first_name="Name1")
        person2 = Person.objects.get(first_name="Name2")
        self.assertEqual(person1.last_name, "Surename1")
        self.assertEqual(person2.last_name, "Surename2")