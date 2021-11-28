import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Dry the rain", "The Beta Band", 6.06)

    def test_song_has_name(self):
        expected = "Dry the rain"
        result = self.song.song_name
        self.assertEqual(expected, result)

    def test_song_has_artist(self):
        expected = "The Beta Band"
        result = self.song.artist
        self.assertEqual(expected, result)

    def test_song_has_length(self):
        expected = 6.06
        result = self.song.song_length
        self.assertEqual(expected, result)
