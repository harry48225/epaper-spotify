import spotify
from PIL import Image, ImageDraw, ImageFont
from ImageCreator import ImageCreator

sp = spotify.Spotify_client()


i = ImageCreator()

while True:
    song = (sp.get_current_song())

    print("track: {}, artist: {}, album: {}, art: {}".format(song.get_track_name(), song.get_artist() ,song.get_album_name(), song.get_album_art_url()))

    i.get_image(song).show()

    input()