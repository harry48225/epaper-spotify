from waveshare_epd import epd2in13_V2
import spotify
import time
from ImageCreator import ImageCreator

from apscheduler.schedulers.background import BackgroundScheduler

print("start")
epd = epd2in13_V2.EPD()
print("display init")
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

i = ImageCreator()
sp = spotify.Spotify_client()
last_song = None

while True:
    current_song = sp.get_current_song()

    # If there is a currently playing song
    if current_song:

        # Only update if the song is new
        if not (last_song and current_song.get_track_name() == last_song.get_track_name()):

            # Display the image
            print("getting image")
            epd.display(epd.getbuffer(i.get_image(current_song)))

    else:

        # Display no song message if the last song wasn't none,
        if last_song:
            print("no song")
            # Create a no song playing message
            epd.display(epd.getbuffer(i.get_no_song_playing_image()))


    last_song = current_song
    time.sleep(2) # Sleep for 2 seconds


