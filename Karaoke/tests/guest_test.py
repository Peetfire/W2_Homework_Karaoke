import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Peter Kay")

    def test_has_name(self):
        expected = "Peter Kay"
        result = self.guest.name
        self.assertEqual(expected, result)
    
    def test_has_cash(self):
        expected = 50.00
        result = self.guest.get_cash()
        self.assertEqual(expected, result)