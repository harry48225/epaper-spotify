from PIL import Image, ImageOps, ImageDraw
import spotify
import requests
from io import BytesIO
url = "https://i.scdn.co/image/ab67616d00001e02792675f3474149244b0a65a2"

class ImageCreator(object):

    def __init__(self):
        self.sp = spotify.Spotify_client()


    def get_album_art(self, url):
        
        response = requests.get(url)

        album_art = Image.open(BytesIO(response.content))

        grey_album_art = ImageOps.grayscale(album_art).resize((128, 128), resample=Image.LANCZOS)
        

        return grey_album_art

    def get_image(self):

        song = self.sp.get_current_song()

        grey_album_art = self.get_album_art(song.get_album_art_url())

        canvas = Image.new('1', (250, 122), 255) # Empty image of the correct size

        canvas.paste(grey_album_art)

        canvas.show()


    

