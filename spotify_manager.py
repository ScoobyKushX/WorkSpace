import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

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
        liked_songs = []
        
        # Fetch top tracks and recently played tracks
        top_tracks = self.sp.current_user_top_tracks(limit=50)['items']
        recently_played = self.sp.current_user_recently_played(limit=50)['items']
        
        # Iterate over top tracks and check for 'track' key
        for item in top_tracks:
            if 'track' in item:
                liked_songs.append(item['track']['id'])
        
        # Iterate over recently played tracks and check for 'track' key
        for item in recently_played:
            if 'track' in item:
                liked_songs.append(item['track']['id'])
        
        return liked_songs


    # New method example: Get the current user's recently played tracks
    def get_recently_played_tracks(self):
        self.refresh_token()  # Ensure the token is refreshed before making the API call
        recently_played = self.sp.current_user_recently_played(limit=50)  # Fetch the recently played tracks
        
        # Extract the track IDs from the response
        track_ids = [item['track']['id'] for item in recently_played['items'] if item['track']]
        
        return track_ids

    # Additional methods should follow the same structure:
    # 1. Call refresh_token()
    # 2. Perform the API call
    # 3. Return the desired data
