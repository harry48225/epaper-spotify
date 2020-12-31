from PIL import Image, ImageOps, ImageDraw, ImageFont

import textwrap
import spotify
import requests
from io import BytesIO
url = "https://i.scdn.co/image/ab67616d00001e02792675f3474149244b0a65a2"

class ImageCreator(object):
    
    
    def __init__(self):
        self.FONT_SIZE = 10
        
        self.font = ImageFont.truetype("font/PressStart2P-Regular.ttf", self.FONT_SIZE)

    def get_album_art(self, url):
        
        response = requests.get(url)

        album_art = Image.open(BytesIO(response.content))

        grey_album_art = ImageOps.grayscale(album_art).resize((128, 128), resample=Image.LANCZOS)
        

        return grey_album_art

    def get_image(self, song):
        grey_album_art = self.get_album_art(song.get_album_art_url())

        canvas = Image.new('1', (250, 122), 255) # Empty image of the correct size

        canvas.paste(grey_album_art)

        draw = ImageDraw.Draw(canvas)

        # Time to draw the artist, album, and track_name
        y = 16

        y = self.draw_wrapped_text(draw, song.get_artist() + ",", self.font, (136,y), self.FONT_SIZE)
        y = self.draw_wrapped_text(draw, "|", self.font, (136,y), self.FONT_SIZE)
        y = self.draw_wrapped_text(draw, song.get_album_name() + ",", self.font, (136,y), self.FONT_SIZE)
        y = self.draw_wrapped_text(draw, "|", self.font, (136,y), self.FONT_SIZE)
        y = self.draw_wrapped_text(draw, song.get_track_name(), self.font, (136,y), self.FONT_SIZE)

        return canvas

    def draw_wrapped_text(self, draw, text, font, position, size):
        # Return the y coordinate of the last line of text

        x = position[0]
        y = position[1]
        for line in textwrap.wrap(text, width=int(100/self.FONT_SIZE)):
            draw.text((x,y), line, font = font, fill = 0)
            y += (size+2)

        return y

    def get_no_song_playing_image(self):

        canvas = Image.new('1', (250, 122), 255) # Empty image of the correct size
        draw = ImageDraw.Draw(canvas)
        draw.text((16,60), "nothing is playing o.O", font = self.font, fill = 0)

        return canvas

    

