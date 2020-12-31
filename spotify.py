import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Song import Song
import yaml


class Spotify_client(object):

    def __init__(self):

        self.CLIENT_ID = None
        self.CLIENT_SECRET = None

        self.load_secrets()

        self.token = None
        self.Spotify = None
        self.sp_oauth = None

        self.authenticate()

    def get_current_song(self):

        if self.sp_oauth.is_token_expired(self.token):
            self.refresh_token()

        recent_songs = self.Spotify.current_user_playing_track()

        track_name = recent_songs['item']['name']
        album_name = recent_songs['item']['album']['name']
        album_art = recent_songs['item']['album']['images'][1]['url'] # Change to 0 to get 64x64 image
        artist = recent_songs['item']['album']['artists'][0]['name'] # Might potentially be multiple artists?

        return Song(track_name, album_name, album_art, artist)

    def load_secrets(self):
        with open("credentials.yaml") as f:

            credential_list = yaml.load(f, Loader=yaml.FullLoader)

            self.CLIENT_ID = credential_list['client-ID']
            self.CLIENT_SECRET = credential_list['client-secret']


    def authenticate(self):

        self.sp_oauth = SpotifyOAuth(client_id=self.CLIENT_ID,client_secret=self.CLIENT_SECRET,redirect_uri="http://hailthealmightyoctopus.xyz",scope="user-read-private, user-read-recently-played, user-read-playback-state, user-read-currently-playing")

        token = self.sp_oauth.get_cached_token()
        if not token:

            auth_url = self.sp_oauth.get_authorize_url()
            print(auth_url)
            response= input("please the above link into your browser then paste the url of the page you get redirected to here: ")

            code = self.sp_oauth.parse_response_code(response)

            token = self.sp_oauth.get_access_token(code, as_dict = True)

        self.token = token
        self.Spotify = spotipy.Spotify(auth=token['access_token'])

    def refresh_token(self):
  
        token_info = self.sp_oauth.refresh_access_token(self.token['refresh_token'])
        self.token = token_info
        self.Spotify = spotipy.Spotify(auth=self.token['access_token'])


