
class Song(object):

    def __init__(self, track_name, album_name, album_art_url, artist):

        self.track_name = track_name
        self.album_name = album_name
        self.album_art_url = album_art_url
        self.artist = artist

    def get_track_name(self):
        return self.track_name

    def get_album_name(self):
        return self.album_name

    def get_album_art_url(self):
        return self.album_art_url

    def get_artist(self):
        return self.artist
        
    def equals(self, song):

        match = True

        match = match and self.track_name == song.get_track_name()

        match = match and self.album_name == song.get_album_name()

        match = match and self.artist == song.get_artist()

        return match