import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("9 to 5", "Dolly Parton", 2.42)
        self.song2 = Song("Me & Bobby McGee", "Janis Joplin", 4.31)
        self.song3 = Song("Just Dropped In", "Kenny Rogers", 3.20)
        self.playlist = [self.song1, self.song2, self.song3]
        self.guest1 = Guest("Peter Kay", 40)
        self.guest2 = Guest("Tom Jones", 60)
        self.guest3 = Guest("Helena Bonham-Carter", 1000)
        self.guest4 = Guest("Sean Locke", 100)
        self.guest5 = Guest("John Bonham", 200)
        self.guest6 = Guest("Frnak Zappa", 400)
        self.group = [self.guest1, self.guest2, self.guest3]
        self.big_group = self.group + [self.guest4, self.guest5]
        self.room = Room("Zulu Lounge", 5)

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
        self.room.add_songs(self.playlist)
        expected = 3
        result = len(self.room.get_songs())
        self.assertEqual(expected, result)

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest1)
        expected = 1
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)

    # @unittest.skip("")
    def test_can_add_guests_to_room(self):
        self.room.add_group(self.group)
        expected = 3
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)

    def test_cannot_add_guest_to_room_no_space(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        self.room.add_guest(self.guest4)
        self.room.add_guest(self.guest5)
        expected = 5
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)
        self.room.add_guest(self.guest6)
        expected = 5
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)
    
    # @unittest.skip("")
    def test_cannot_add_guests_to_room_no_space(self):
        self.room.add_group(self.group)
        expected = 3
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)
        self.room.add_group(self.group)
        expected = 3
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)

    def test_can_remove_guest_from_room(self):
        self.room.add_guest(self.guest1)
        self.room.remove_guest(self.guest1)
        expected = 0
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)

    # @unittest.skip("")
    def test_can_remove_group_of_guests_from_room(self):
        self.room.add_group(self.group)
        self.room.remove_group(self.group)
        expected = 0
        result = len(self.room.get_guests())
        self.assertEqual(expected, result)

    
