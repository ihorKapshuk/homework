from task1 import File
import unittest

class TestMyTask(unittest.TestCase):

    def test_file_working(self):
        with File("lesson21/my_test.txt", "w") as my_test:
            my_test.write("Hi!\n")
        with File("lesson21//my_test.txt", "r") as my_test:
            result = my_test.read()
        self.assertEqual("Hi!\n", result)
    
    def test_logs(self):
        with open("lesson21/logs.txt", "r") as my_logs:
            result = my_logs.readlines()
        self.assertIn("1", result[0])
        self.assertIn("w", result[1])
        self.assertIn("2", result[3])
        self.assertIn("r", result[4])

if __name__ == "__main__":
    unittest.main()