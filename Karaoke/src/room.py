class Room:

    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs