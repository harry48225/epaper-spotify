from waveshare_epd import epd2in13_V2
import spotify
import time
from ImageCreator import ImageCreator


class App(object):

    def __init__(self):
        
        print("start")
        self.epd = epd2in13_V2.EPD()
        print("display init")
        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.Clear(0xFF)


        self.i = ImageCreator()
        self.sp = spotify.Spotify_client()
        self.last_song = None

    def update(self):

        current_song = self.sp.get_current_song()

        # If there is a currently playing song
        if current_song:

            # Only update if the song is new
            if not (self.last_song and self.last_song.equals(current_song)):

                # Display the image
                print("getting image")
                self.epd.display(self.epd.getbuffer(self.i.get_image(current_song)))

        else:

            # Display no song message if the last song wasn't none,
            if self.last_song:
                print("no song")
                # Create a no song playing message
                self.epd.display(self.epd.getbuffer(self.i.get_no_song_playing_image()))


        self.last_song = current_song