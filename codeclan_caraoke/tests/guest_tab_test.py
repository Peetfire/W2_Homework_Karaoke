import unittest
from src.guest_tab import Guest_tab
from src.refreshment import Refreshment

class TestGuest_tab(unittest.TestCase):
    def setUp(self):
        self.tab = Guest_tab("Jonny")
        self.item1 = Refreshment("Crisps", 1.50, 2)
        self.item2 = Refreshment("Beer", 3.50, 5)
        self.item3 = Refreshment("Coke", 2.00, 1)
        self.item_list = [self.item1, self.item2, self.item3]

    def test_has_name(self):
        expected = "Jonny"
        result = self.tab.name
        self.assertEqual(expected, result)

    def test_has_item_list(self):
        expected = 0
        result = len(self.tab.items)
        self.assertEqual(expected, result)