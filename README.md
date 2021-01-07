# epaper-spotify
Show the currently playing spotify song on an RPi attached e-paper- 
designed for a pi zero with a 2.13" waveshare epaper display.

Get's the album art, and info about the user's currently playing song on spotify every 2 seconds and displays it on the epaper screen.

![Image of the project](https://github.com/harry48225/epaper-spotify/blob/master/example.jpg)

Close up the image looks a little fragmented but this is just ![dithering](https://en.wikipedia.org/wiki/Dither), from a reasonable distance the effect is pretty convincing.

Place Spotify API credentials in ```credentials.yaml```
Then run ```pip install -r requirements.txt``` (a venv might be helpful)
and run the program with ```python main.py```
The program will guide you through linking it to spotify
