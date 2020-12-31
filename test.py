import spotify
import ImageCreator

sp = spotify.Spotify_client()

song = (sp.get_current_song())

print("track: {}, artist: {}, album: {}, art: {}".format(song.get_track_name(), song.get_artist() ,song.get_album_name(), song.get_album_art_url()))