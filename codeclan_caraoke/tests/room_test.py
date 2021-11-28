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
        self.guest1 = Guest("Peter Kay", 50, "")
        self.guest2 = Guest("Tom Jones", 60, "Just Dropped In")
        self.guest3 = Guest("Helena Bonham-Carter", 1000, "9 to 5")
        self.guest4 = Guest("Sean Locke", 100, "Me & Bobby McGee")
        self.guest5 = Guest("John Bonham", 200, "Just Dropped In")
        self.guest6 = Guest("Frank Zappa", 40, "Just Dropped In")
        self.group = [self.guest1, self.guest2, self.guest3]
        self.big_group = self.group + [self.guest4, self.guest5]
        self.group_cant_all_pay = [self.guest1, self.guest2, self.guest6]
        self.room = Room("Zulu Lounge", 5, 50)

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

    def test_there_is_capacity(self):
        self.room.add_group(self.group)
        result = self.room.is_capacity(2)
        self.assertTrue(result)

    def test_there_is_not_capacity(self):
        self.room.add_group(self.group)
        result = self.room.is_capacity(3)
        self.assertFalse(result)

    def test_charge_entry_fee_can_pay(self):
        self.room.sell_tickets(self.guest3)
        expected_g_no = 1
        guest_no_result = len(self.room.get_guests())
        expected_take = 50
        takings_result = self.room.get_takings()
        expected_cash = 950
        result_cash = self.guest3.get_cash()
        self.assertEqual(expected_g_no, guest_no_result)
        self.assertEqual(expected_take, takings_result)
        self.assertEqual(expected_cash, result_cash)

    def test_charge_entry_fee_cannot_pay(self):
        self.room.sell_tickets(self.guest6)
        expected_g_no = 0
        guest_no_result = len(self.room.get_guests())
        expected_take = 0
        takings_result = self.room.get_takings()
        expected_cash = 40
        result_cash = self.guest6.get_cash()
        self.assertEqual(expected_g_no, guest_no_result)
        self.assertEqual(expected_take, takings_result)
        self.assertEqual(expected_cash, result_cash)


    def test_charge_entry_fee_group_can_pay(self):
        self.room.sell_tickets(self.group)
        expected_g = 3
        guest_no_result = len(self.room.get_guests())
        expected_t = 150
        takings_result = self.room.get_takings()
        expected1 = 0
        expected2 = 10
        expected3 = 950
        result1 = self.guest1.get_cash()
        result2 = self.guest2.get_cash()
        result3 = self.guest3.get_cash()
        self.assertEqual(expected_g, guest_no_result)
        self.assertEqual(expected_t, takings_result)
        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)
        self.assertEqual(expected3, result3)

    def test_charge_entry_fee_group_cant_all_pay(self):
        self.room.sell_tickets(self.group_cant_all_pay)
        expected_g = 2
        guest_no_result = len(self.room.get_guests())
        expected_t = 100
        takings_result = self.room.get_takings()
        expected1 = 0
        expected2 = 10
        expected3 = 40
        result1 = self.guest1.get_cash()
        result2 = self.guest2.get_cash()
        result3 = self.guest6.get_cash()
        self.assertEqual(expected_g, guest_no_result)
        self.assertEqual(expected_t, takings_result)
        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)
        self.assertEqual(expected3, result3)

    def test_can_check_for_fave_song_True(self):
        result = self.room.is_fave_song(self.song3, self.guest6)
        expected = True
        self.assertEqual(expected ,result)

    def test_can_check_for_fave_song_False(self):
        result = self.room.is_fave_song(self.song3, self.guest1)
        expected = False
        self.assertEqual(expected ,result)

    def test_room_can_play_song(self):
        self.room.add_group(self.big_group)
        result = self.room.play_song(self.song3, self.guest5)
        expected = "Now playing: Just Dropped In by Kenny Rogers for John"
        self.assertEqual(expected ,result)




    
