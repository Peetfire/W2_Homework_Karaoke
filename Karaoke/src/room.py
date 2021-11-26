class Room:

    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def add_songs(self, songs):
        self.songs.extend(songs)

    def get_songs(self):
        return self.songs

    def add_guest(self, guest):
        self.guests.append(guest)

    def add_group(self, group):
        self.guests.extend(group)

    def get_guests(self):
        return self.guests

    def remove_guest(self, guest):
        self.guests.remove(guest)

    def remove_group(self, group):
        for guest in group:
            if guest in self.guests:
                self.guests.remove(guest) 