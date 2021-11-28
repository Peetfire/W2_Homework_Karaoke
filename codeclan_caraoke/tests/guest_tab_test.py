import unittest
from src.guest_tab import Guest_tab
from src.refreshment import Refreshment

class TestGuest_tab(unittest.TestCase):
    def setUp(self):
        self.tab = Guest_tab("Jonny")
        self.item1 = Refreshment("Crisps", 1.50, 2)
        self.item2 = Refreshment("Beer", 3.50, 5)
        self.item3 = Refreshment("Coke", 2.00, 1)

    def test_has_name(self):
        expected = "Jonny"
        result = self.tab.name
        self.assertEqual(expected, result)

    def test_has_item_list(self):
        expected = 0
        result = len(self.tab.items)
        self.assertEqual(expected, result)

    def test_can_add_item(self):
        self.tab.add_item(self.item1)
        expected = 1
        result = len(self.tab.items)
        self.assertEqual(expected, result)

    def test_can_get_tab_value(self):
        self.tab.add_item(self.item1)
        self.tab.add_item(self.item2)
        self.tab.add_item(self.item3)
        expected = 22.50
        result = self.tab.get_tab_value()
        self.assertEqual(expected, result)