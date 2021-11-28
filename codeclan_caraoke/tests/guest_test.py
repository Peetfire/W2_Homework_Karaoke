import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Peter Kay", 50.00, "Madness")
        self.song = Song("Madness", "Prince Buster", 2.34)

    def test_has_name(self):
        expected = "Peter Kay"
        result = self.guest.name
        self.assertEqual(expected, result)
    
    def test_has_cash(self):
        expected = 50.00
        result = self.guest.get_cash()
        self.assertEqual(expected, result)

    def test_can_pay_entry_fee(self):
        result1 = self.guest.pay_entry_fee(15)
        self.assertTrue(result1)
        expected = 35
        result2 = self.guest.get_cash()
        self.assertEqual(expected, result2)

    def test_cannot_pay_entry_fee(self):
        result1 = self.guest.pay_entry_fee(60)
        self.assertFalse(result1)
        expected = 50
        result2 = self.guest.get_cash()
        self.assertEqual(expected, result2)

    def test_can_shout_out(self):
        result_guest = self.guest.get_shout_out()
        expected_guest = "Ya, dancer!"
        self.assertEqual(expected_guest ,result_guest)
        