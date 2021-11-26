import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("9 to 5", "Dolly Parton", 2.42)
        self.song2 = Song("Me & Bobby McGee", "Janis Joplin", 4.31)
        self.song3 = Song("Just Dropped In", "Kenny Rogers", 3.20)
        self.guest1 = Guest("Peter Kay")
        self.guest2 = Guest("Tom Jones")
        self.guest3 = Guest("Helena Bonham-Carter")
        self.room = Room("Zulu Lounge")

    def test_room_has_name(self):
        expected = "Zulu Lounge"
        result = self.room.name
        self.assertEqual(expected, result)
