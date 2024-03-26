import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Musique.spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtCore import Qt
class SpotifyManager:
    def __init__(self):
        try:
            scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-private user-top-read user-read-recently-played"
            self.auth_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI, scope=scope, cache_path="token_cache.txt")
            self.sp = spotipy.Spotify(auth_manager=self.auth_manager)
            if not self.auth_manager.get_cached_token():
                self.auth_manager.get_access_token(as_dict=False)
        except Exception as e:
            print(f"An error occurred while authenticating with Spotify: {str(e)}")

    def refresh_token(self):
        if self.auth_manager.is_token_expired(self.auth_manager.get_cached_token()):
            self.auth_manager.refresh_access_token(self.auth_manager.get_cached_token()['refresh_token'])


    def get_unique_liked_songs(self):
        self.refresh_token()
        
        top_tracks = self.sp.current_user_top_tracks(limit=50)['items']
        recently_played = self.sp.current_user_recently_played(limit=50)['items']# The backtick
        recently_played_2 = self.sp.current_user_recently_played(limit=50, after=recently_played[-1]['played_at'])['items'] #  
        recently_played_3 = self.sp.current_user_recently_played(limit=50, after=recently_played_2[-1]['played_at'])['items']
        recently_played_4 = self.sp.current_user_recently_played(limit=50, after=recently_played_3[-1]['played_at'])['items']
        recently_played_5 = self.sp.current_user_recently_played(limit=50, after=recently_played_4[-1]['played_at'])['items']
        recently_played = recently_played + recently_played_2 + recently_played_3 + recently_played_4 + recently_played_5
        top_tracks_2 = self.sp.current_user_top_tracks(limit=50, offset=50)['items']
        top_tracks_3 = self.sp.current_user_top_tracks(limit=50, offset=100)['items']
        top_tracks_4 = self.sp.current_user_top_tracks(limit=50, offset=150)['items']
        top_tracks_5 = self.sp.current_user_top_tracks(limit=50, offset=200)['items']
        top_tracks_6 = self.sp.current_user_top_tracks(limit=50, offset=250)['items']
        top_tracks_7 = self.sp.current_user_top_tracks(limit=50, offset=300)['items']
        top_tracks_8 = self.sp.current_user_top_tracks(limit=50, offset=350)['items']
        top_tracks_9 = self.sp.current_user_top_tracks(limit=50, offset=400)['items']
        top_tracks_10 = self.sp.current_user_top_tracks(limit=50, offset=450)['items']
        top_tracks = top_tracks + top_tracks_2 + top_tracks_3 + top_tracks_4 + top_tracks_5 + top_tracks_6 + top_tracks_7 + top_tracks_8 + top_tracks_9 + top_tracks_10
        unique_tracks = []
        for track in top_tracks:
            if track['id'] not in [t['id'] for t in unique_tracks]:
                unique_tracks.append(track)

        for item in recently_played:
            track = item['track']
            if track['id'] not in [t['id'] for t in unique_tracks]:
                unique_tracks.append(track)

        return unique_tracks
        
            
    def play_music(self, track_id=None):
        try:
            self.refresh_token()
            if track_id:
                self.sp.start_playback(uris=[f'spotify:track:{track_id}'])
            else:
                print("Aucun identifiant de piste fourni.")
        except spotipy.SpotifyException as e:
            print(f"Erreur lors de la tentative de jouer la piste : {e}")
                # Additional methods should follow the same structure:
            # 1. Call refresh_token()
            # 2. Perform the API call
            # 3. Return the desired data
            
    def stop_music(self):
        self.refresh_token()
        self.sp.pause_playback()