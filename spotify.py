import spotipy
from spotipy.oauth2 import SpotifyOAuth

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
        recent_songs = self.Spotify.current_user_playing_track()

        print(recent_songs)

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

            token = self.sp_oauth.get_access_token(code, as_dict = False)
        else:
            token = token['access_token']

        self.Spotify = spotipy.Spotify(auth=token)

    def refresh_token(self):
        if self.sp_oauth.is_token_expired(token_info):
            token_info = self.sp_oauth.refresh_access_token(token_info['refresh_token'])
            token = token_info['access_token']
            self.Spotify = spotipy.Spotify(auth=token)


