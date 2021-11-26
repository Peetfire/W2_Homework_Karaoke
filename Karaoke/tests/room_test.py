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

    def test_room_has_song_list(self):
        expected = 0
        result = len(self.room.songs)
        self.assertEqual(expected, result)

    def test_room_has_guest_list(self):
        expected = 0
        result = len(self.room.guests)
        self.assertEqual(expected, result)

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song1)
        expected = 1
        result = len(self.room.get_songs())
        self.assertEqual(expected, result)

    def test_can_add_songs_to_room(self):
        self.room.add_song(self.song1)
        self.room.add_song(self.song2)
        self.room.add_song(self.song3)
        expected = 3
        result = len(self.room.get_songs())
        self.assertEqual(expected, result)

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest1)
        expected = 1
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)

    def test_can_add_guests_to_room(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        expected = 3
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)
