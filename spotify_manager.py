import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from PySide6.QtWidgets import QTableWidgetItem

class SpotifyManager:
    def __init__(self):
        self.sp = None
        try:
            self.auth_manager = SpotifyOAuth(
                client_id=SPOTIFY_CLIENT_ID,
                client_secret=SPOTIFY_CLIENT_SECRET,
                redirect_uri=SPOTIFY_REDIRECT_URI,
                scope="user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private user-top-read user-read-recently-played",
                cache_path="token_cache.txt"  # This file stores the token information
            )
            # Check if a valid access token is available
            if not self.auth_manager.get_cached_token():
                self.auth_manager.get_access_token(as_dict=False)
            self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
        except Exception as e:
            print(f"An error occurred while authenticating with Spotify: {str(e)}")

    def refresh_token(self):
        # Refresh the access token
        if self.auth_manager.is_token_expired(self.auth_manager.get_cached_token()):
            self.auth_manager.refresh_access_token(self.auth_manager.get_cached_token()['refresh_token'])

    def get_unique_liked_songs(self):
        self.refresh_token()
        top_tracks = self.sp.current_user_top_tracks(limit=50)['items']
        recently_played = self.sp.current_user_recently_played(limit=50)['items']

        track_ids = set()
        unique_tracks = []

        for track in top_tracks:
            if 'id' in track and track['id'] not in track_ids:
                unique_tracks.append(track)
                track_ids.add(track['id'])

        for item in recently_played:
            # 'track' key might be nested within 'item' for recently played tracks
            if 'track' in item and 'id' in item['track'] and item['track']['id'] not in track_ids:
                unique_tracks.append(item['track'])
                track_ids.add(item['track']['id'])

        return unique_tracks

    def populate_playlist_table(self):
        unique_tracks = self.get_unique_liked_songs()

        self.ui.tableWidget_3.setRowCount(len(unique_tracks))

        for i, track in enumerate(unique_tracks):
            # Using 'name' to fetch the track name
            # Ensure 'name' is present in the track dictionary
            track_name = track['track']['name'] if 'name' in track['track'] else 'Unknown Name'
            self.ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(track_name))


        # Additional methods should follow the same structure:
        # 1. Call refresh_token()
        # 2. Perform the API call
        # 3. Return the desired data
