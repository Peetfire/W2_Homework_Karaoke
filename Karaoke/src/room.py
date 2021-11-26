from typing import List


class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.guests = []
        self.songs = []
        self.capacity = capacity

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