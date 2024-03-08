import os
from PySide6.QtCore import QTimer
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget, \
    QTableWidget, QPlainTextEdit, QPushButton
from matplotlib.backends.backend_template import FigureCanvas

from ui_your_interface import Ui_MainWindow
from spotify_manager import SpotifyManager
from audio_visual import RealTimeAudioVisualizer
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.sp_manager = SpotifyManager()
        self.setup_ui()  # Ensure setup_ui is called to setup the tabs and layouts
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.audiovisualizer.update_plot)
        self.timer.start(100)  # Adjust the interval as needed
        self.populate_playlist_with_liked_songs()
        self.tableWidget.itemClicked.connect(self.play_selected_music)
        self.audiovisualizer = RealTimeAudioVisualizer()  # Create the visualizer instance
        self.widget.setLayout(self.audiovisualizer)  # Add the visualizer instance to the layout
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
        self.MontageVideo = QWidget()
        self.AI = QWidget()
        self.perso = QWidget()
        self.jeux = QWidget()

        # Setup for the "Musique" tab
        self.musiquelayout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(0, 831)
        self.tableWidget.setHorizontalHeaderLabels(['Tracks'])
        self.musiquelayout.addWidget(self.tableWidget)
        self.musique.setLayout(self.musiquelayout)
        self.widget.setLayout(self.musiquelayout)

        layout = QVBoxLayout()  # Create a layout
        self.audiovisualizer = RealTimeAudioVisualizer()  # Create the visualizer instance
        layout.addWidget(self.audiovisualizer)  # Add the visualizer instance to the layout
        self.widget.setLayout(layout)  # Correctly set layout to the widget


        self.persoLayout = QVBoxLayout()
        self.textEdit = QPlainTextEdit()
        self.saveButton = QPushButton("Save Notes")
        self.saveButton.clicked.connect(self.save_notes)

        self.persoLayout.addWidget(self.textEdit)
        self.persoLayout.addWidget(self.saveButton)
        self.perso.setLayout(self.persoLayout)

        self.tabs.addTab(self.musique, "Musique & Plus")
        self.tabs.addTab(self.programmation, "Programmation")
        self.tabs.addTab(self.MontageVideo, "Montage Vidéo")
        self.tabs.addTab(self.AI, "AI")
        self.tabs.addTab(self.perso, "Perso")
        self.tabs.addTab(self.jeux, "Jeux")

        self.setCentralWidget(self.tabs)
        self.populate_playlist_with_liked_songs()  # Populate with your playlist
        self.show()

    def save_notes(self):
        content = self.textEdit.toPlainText()
        filename = QDate.currentDate().toString("yyyy-MM-dd") + ".txt"
        filepath = os.path.join("notes", filename)  # Save in a "notes" directory
        os.makedirs("notes", exist_ok=True)  # Ensure the directory exists
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        QMessageBox.information(self, "Saved", f"Notes saved to {filename}")
