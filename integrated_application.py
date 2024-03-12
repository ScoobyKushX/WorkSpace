
# Integrated Script

import os
import sys

from PySide6.QtGui import QScreen

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://localhost:8888/callback"


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtCore import QTimer, QFile
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget, QTableWidget

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
        results = self.sp.current_user_saved_tracks(limit=50)
        for item in results['items']:
            track_id = item['track']['id']
            liked_songs.add(item['id'])

        top_tracks = self.sp.current_user_top_tracks(limit=50)['items']
        for track in top_tracks:
            liked_songs.add(track['id'])
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


import numpy as np
import pyaudio
from scipy.fft import fft  # Utilisation de scipy.fft qui remplace scipy.fftpack
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import cm

class RealTimeAudioVisualizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_audio_stream()
        self.init_ui()

    def init_audio_stream(self):
        self.audio_format = pyaudio.paFloat32
        self.channels = 2
        self.sample_rate = 44800
        self.chunk_size = 1024
        self.audio_stream = pyaudio.PyAudio().open(format=self.audio_format, channels=self.channels,
                                                   rate=self.sample_rate, input=True, frames_per_buffer=self.chunk_size)

    def init_ui(self):
        fig = Figure()
        self.canvas = FigureCanvas(fig)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

        self.audio_ax = fig.add_subplot(211)
        self.spectrogram_ax = fig.add_subplot(212)

        self.x_audio = np.arange(0, 2 * self.chunk_size, 2)
        self.y_audio = np.zeros(self.chunk_size)
        self.line, = self.audio_ax.plot(self.x_audio, self.y_audio, color='c')

        self.audio_ax.set_xlim(0, self.chunk_size)
        self.audio_ax.set_ylim(-2 ** 15, 2 ** 15)

        self.timer = self.canvas.new_timer(50)
        self.timer.add_callback(self.update_plot)
        self.timer.start()

    def update_plot(self):
        audio_data = np.frombuffer(self.audio_stream.read(self.chunk_size), np.int16)
        self.line.set_ydata(audio_data)

        fft_data = np.abs(fft(audio_data))[:self.chunk_size // 2]
        self.spectrogram_ax.clear()
        self.spectrogram_ax.plot(fft_data, color=cm.plasma(np.max(fft_data) / np.max(fft_data)))

        self.canvas.draw()

    def closeEvent(self, event):
        self.timer.stop()
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        pyaudio.PyAudio().terminate()


import os
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget, QTableWidget

from PySide6.QtUiTools import QUiLoader, QIntList
from spotify_manager import SpotifyManager
from audio_visual import RealTimeAudioVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loader = QUiLoader()
        file = QFile("form.ui")
        file.open(QFile.ReadOnly)

        self.sp_manager = SpotifyManager()
        self.audiovisualizer = RealTimeAudioVisualizer(self)

        self.ui = loader.load(file, self)
        file.close()
        self.setup_ui()
        self.setup_visualizer()
        self.setup_playlist()

    def setup_visualizer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.audiovisualizer.update_plot)
        self.timer.start(100)  # Update interval in milliseconds

    def setup_playlist(self):
        self.populate_playlist_with_liked_songs()
        self.tableWidget.itemClicked.connect(self.play_selected_music)

    def populate_playlist_with_liked_songs(self):
        try:
            unique_song_ids = self.sp_manager.get_unique_liked_songs()
            self.tableWidget.setRowCount(len(unique_song_ids))
            for i, track_id in enumerate(unique_song_ids):
                track_details = self.sp_manager.sp.track(track_id)
                track_name = f"{track_details['artists'][0]['name']} - {track_details['name']}"
                self.tableWidget.setItem(i, 0, QTableWidgetItem(track_name))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load liked songs: {str(e)}")

    def play_selected_music(self, item):
        track_id = self.sp_manager.get_unique_liked_songs()[self.tableWidget.row(item)]
        try:
            self.sp_manager.play_music(track_id=track_id)
        except Exception as e:
            QMessageBox.critical(self, "Playback Error", f"An error occurred during playback: {str(e)}")

    def setup_ui(self):
        self.tabs = QTabWidget()
        self.musique = QWidget()
        self.programmation = QWidget()
        self.montageVideo = QWidget()
        self.ai = QWidget()
        self.perso = QWidget()
        self.jeux = QWidget()

        # Setup for the "Musique" tab
        self.musiqueLayout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(0, 831)
        self.tableWidget.setHorizontalHeaderLabels(['Tracks'])
        self.musiqueLayout.addWidget(self.tableWidget)
        self.musique.setLayout(self.musiqueLayout)

        # Additional tab setups should be added here...

        # Adding tabs to the main window
        self.tabs.addTab(self.musique, "Musique")
        self.tabs.addTab(self.programmation, "Programmation")
        self.tabs.addTab(self.montageVideo, "Montage Video")
        self.tabs.addTab(self.ai, "AI")
        self.tabs.addTab(self.perso, "Perso")
        self.tabs.addTab(self.jeux, "Jeux")

        self.setCentralWidget(self.tabs)






