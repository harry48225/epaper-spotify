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


    # Only update if the song is new
    if not (last_song and current_song.get_track_name() == last_song.get_track_name()):

        # Display the image
        print("getting image")
        epd.display(epd.getbuffer(i.get_image(current_song)))

        last_song = current_song

    time.sleep(10) # Sleep for 10 seconds


