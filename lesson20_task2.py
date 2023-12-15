import unittest
from os import path
import lesson11.module as pb
import json

class ExistanceChecker:

    def is_file_exist(self, filepath : str):
        return path.exists(filepath)
    
    def checker(self, filepath):
        result = self.is_file_exist(filepath)
        if result:
            return 1
        else:
            return 0

class TestPhoneBookMaking(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file = "test_phonebook.json"

    def test_make_phonebook(self):
        pb.make_phonebook(self.test_file)
        ch = ExistanceChecker()
        self.assertEqual(ch.checker(self.test_file), 1)

class TestPhoneBookTools(unittest.TestCase):

    def setUp(self) -> None:
        self.test_file = "test_phonebook.json"

    def test_add_record(self):
        pb.add_record("Name", "Surename", "0987654321", "Odesa", self.test_file)
        with open(self.test_file) as read_test:
            content = json.load(read_test)
            self.assertEqual(content[len(content) - 1], {"first_name": "Name", "last_name": "Surename", "tel_number": "0987654321", "city": "Odesa"})
    
    def test_find_record(self):
        result = pb.find_record("Name", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("Surename", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("0987654321", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("Odesa", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("Name Surename", self.test_file)
        self.assertEqual(result, 1)
        result = pb.find_record("qwerty", self.test_file)
        self.assertEqual(result, 2)
    
    def test_update_record(self):
        pb.update_record("0987654321", "0957654321", self.test_file)
        with open(self.test_file) as read_test:
            content = json.load(read_test)
            self.assertEqual(content[0]["tel_number"], "0957654321")

    def test_delete_record(self):
        pb.delete_record("0957654321", self.test_file)
        result = pb.find_record("0957654321", self.test_file)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()