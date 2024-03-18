from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidget
from ui_main_window import Ui_MainWindow
from spotify_manager import SpotifyManager
from Chords_generator import PartitionWidget


#from audio_visual import RealTimeAudioVisualizer

class MainWindow(parent=None):
    def __init__(self, parent=Ui_MainWindow):
        super(MainWindow, self).__init__(parent=None)
        self.sp_manager = SpotifyManager()  # Initialise SpotifyManager
        self.ui = Ui_MainWindow()  # Crée une instance de l'interface utilisateur
        self.ui.setupUi(self)  # Charge l'interface utilisateur
        self.populate_playlist_table
        self.ui.gridLayout_14.addWidget(self.ui.tabWidget_3, 0, 0, 1, 1)
        self.ui.gridLayout_14.addWidget(self.ui.progressBar_3, 1, 0, 1, 1)
        self.ui.progressBar_3.setMaximum(100)



    def on_button_click(self):
        try:
            selected_music = self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text()
            print(f"Playing: {selected_music}")
        except AttributeError:
            print("No music selected. Please select a music from the table.")
    # Cette fonction semble être référencée mais n'est pas définie.
    # Définissons-la pour éviter les erreurs.
    def on_text_edit_change(self):
        print("Text changed!")

    def on_slider_value_change(self, value):
        print(f"Slider value changed: {value}")

    def populate_playlist_table(self):
    # Récupère les playlists de l'utilisateur
        playlists = self.sp_manager.get_user_playlists()

        # Configure le QTableWidget
        self.ui.playlistTable.setRowCount(len(playlists))
        self.ui.playlistTable.setColumnCount(2)  # Par exemple, 'Nom de la playlist' et 'Nombre de titres'
        self.ui.playlistTable.setHorizontalHeaderLabels(['Playlist Name', 'Number of Tracks'])

        # Remplit le tableau avec les données des playlists
        for i, playlist in enumerate(playlists):
            self.ui.playlistTable.setItem(i, 0, QTableWidgetItem(playlist['name']))
            self.ui.playlistTable.setItem(i, 1, QTableWidgetItem(str(playlist['tracks']['total'])))

    def generate_chords(self):
        print("generate_chords clicked!")

    def update_progress_bar(self, value):
        if 0 <= value <= 100:
            self.ui.progressBar_3.setValue(value)
        else:
            print("Invalid value for progress bar.")