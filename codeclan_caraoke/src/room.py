from typing import List


class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.takings = 0

    def add_song(self, song):
        self.songs.append(song)

    def add_songs(self, songs):
        self.songs.extend(songs)

    def get_songs(self):
        return self.songs

    def get_remaining_cap(self):
        return self.capacity - len(self.get_guests())

    def is_capacity(self, amount):
        return self.get_remaining_cap() >= amount

    def get_price(self):
        return self.entry_fee

    def add_guest(self, guest):
        if self.is_capacity(1):
            self.guests.append(guest)

    def add_group(self, group):
        if self.is_capacity(len(group)):
            self.guests.extend(group)

    def get_guests(self):
        return self.guests

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def remove_group(self, group):
        for guest in group:
            if guest in self.guests:
                self.guests.remove(guest) 

    def increase_takings(self, amount):
        self.takings += amount

    def get_takings(self):
        return self.takings

    def sell_tickets(self, guests):
        if type(guests) == list:
            for guest in guests:
                if guest.get_cash() >= self.get_price():
                    guest.reduce_cash(self.get_price())
                    self.increase_takings(self.get_price())
                    self.add_guest(guest)
        else:
            guest = guests
            if guest.get_cash() >= self.get_price():
                guest.reduce_cash(self.get_price())
                self.increase_takings(self.get_price())
                self.add_guest(guest)

    def play_song(self, song, selector):
        # Displays song details currently playing
        print(f"\nNow playing: {song.song_name} by {song.artist} for {selector.name.split()[0]}")
        
        # Check all guests to see if their favourite song is playing and IF it is
        # displays their shout out.
        for guest in self.guests:
            if self.is_fave_song(song, guest):
                print(f"{guest.name.split()[0]} shouts out: {guest.get_shout_out()}")

        return f"Now playing: {song.song_name} by {song.artist} for {selector.name.split()[0]}"

    def is_fave_song(self, song, guest):
        return song.song_name == guest.get_fave_song()
