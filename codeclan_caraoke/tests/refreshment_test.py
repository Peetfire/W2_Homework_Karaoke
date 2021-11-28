import unittest
from src.refreshment import Refreshment

class TestRefreshment(unittest.TestCase):
    def setUp(self):
        self.item = Refreshment("Crisps", 1.50, 20)

    def test_has_name(self):
        expected = "Crisps"
        result = self.item.name
        self.assertEqual(expected, result)

    def test_has_price(self):
        expected = 1.50
        result = self.item.price
        self.assertEqual(expected, result)

    def test_has_stock(self):
        expected = 20
        result = self.item.quantity
        self.assertEqual(expected, result)