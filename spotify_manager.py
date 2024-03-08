import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from PySide6.QtWidgets import QMessageBox
class SpotifyManager:
    def __init__(self):
        try:
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_CLIENT_ID,
                client_secret=SPOTIFY_CLIENT_SECRET,
                redirect_uri=SPOTIFY_REDIRECT_URI,
                scope="user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private user-top-read user-read-recently-played"
            ))
        except Exception as e:
            QMessageBox.critical(None, "Spotify Error", f"An error occurred while authenticating with Spotify: {str(e)}")
    def get_unique_liked_songs(self):
        liked_songs = set()
        results = self.sp.current_user_saved_tracks(limit=20)
        for item in results['items']:
            track_id = item['track']['id']
            liked_songs.add(track_id)

        top_tracks = self.sp.current_user_top_tracks(limit=50)['items']
        for track in top_tracks:
            liked_songs.add(track['id'])

        recently_played = self.sp.current_user_recently_played(limit=50)['items']
        for item in recently_played:
            liked_songs.add(item['track']['id'])

        return list(liked_songs)

    def play_music(self, track_id=None):
        devices = self.sp.devices()
        if devices['devices']:
            device_id = devices['devices'][0]['id']
            if track_id:
                self.sp.start_playback(device_id=device_id, uris=[f'spotify:track:{track_id}'])
            else:
                print("No track ID provided.")
        else:
            print("No active devices found. Please ensure the Spotify client is open.")