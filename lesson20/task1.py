import unittest
from lesson15.task3 import TVController

class ControllerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = TVController(["BBC", "Discovery", "TV1000"])
    
    def test_start_channel(self):
        self.assertEqual(self.controller.turned_channel, "BBC")
    
    def test_first_channel(self):
        self.assertEqual(self.controller.first_channel(), "BBC")

    def test_last_channel(self):
        self.assertEqual(self.controller.last_channel(), "TV1000")
    
    def test_turn_channel(self):
        self.assertEqual(self.controller.turn_channel(1), "BBC")
    
    def test_next_channel(self):
        self.assertEqual(self.controller.next_channel(), "Discovery")
    
    def test_previous_channel(self):
        self.controller.turn_channel(2)
        self.assertEqual(self.controller.previous_channel(), "BBC")
    
    def test_current_channel(self):
        self.assertEqual(self.controller.current_channel(), "BBC")
    
    def test_exists(self):
        self.assertEqual(self.controller.exists(1), "Yes")
        self.assertEqual(self.controller.exists(2), "Yes")
        self.assertEqual(self.controller.exists(3), "Yes")
        self.assertEqual(self.controller.exists(4), "No")
        self.assertEqual(self.controller.exists(0), "No")
        self.assertEqual(self.controller.exists("BBC"), "Yes")
        self.assertEqual(self.controller.exists("Discovery"), "Yes")
        self.assertEqual(self.controller.exists("TV1000"), "Yes")
        self.assertEqual(self.controller.exists("National Geografic"), "No")

if __name__ == "__main__":
    unittest.main()