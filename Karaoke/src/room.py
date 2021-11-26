class Room:

    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def add_song(self, song):
        self.guests.append(song)