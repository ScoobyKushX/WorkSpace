import PySide6.QtWidgets, PySide6.QtGui, PySide6.QtCore, PySide6.QtUiTools
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QTableWidget
from ui_main_window import Ui_MainWindow
from spotify_manager import SpotifyManager
from Chords_generator import PartitionWidget


#from audio_visual import RealTimeAudioVisualizer

class MainWindow(QMainWindow):
    def __init__(self, parent=Ui_MainWindow):
        super(MainWindow, self).__init__(parent=None)
        self.sp_manager = SpotifyManager()  # Initialise SpotifyManager
        self.ui = Ui_MainWindow()  # Crée une instance de l'interface utilisateur
        self.ui.setupUi(self)  # Charge l'interface utilisateur
        self.populate_with_good_songs
        self.ui.gridLayout_14.addWidget(self.ui.tabWidget_3, 0, 0, 1, 1)
        self.ui.progressBar_3 = QProgressBar(self.ui.centralwidget)
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

    def populate_with_good_songs(self):
        try:
            unique_song_ids = self.sp_manager.get_unique_liked_songs()
            self.ui.tableWidget_3.setRowCount(len(unique_song_ids))

            for i, track_id in enumerate(unique_song_ids):
                try:
                    track_details = self.sp_manager.sp.track(track_id)
                    track_name = f"{track_details['artists'][0]['name']} - {track_details['name']}"
                    self.ui.tableWidget_3.setItem(i, 0, QTableWidgetItem(track_name))
                except Exception as e_inner:
                    print(f"Error loading song details for track ID {track_id}: {str(e_inner)}")
                    QMessageBox.critical(self, "Error",
                                         f"Failed to load song details for track ID {track_id}: {str(e_inner)}")
        except Exception as e:
            print(f"Failed to load liked songs: {str(e)}")
            QMessageBox.critical(self, "Error", f"Failed to load liked songs: {str(e)}")
            return 

    def generate_chords(self):
        print("generate_chords clicked!")

    def update_progress_bar(self, value):
        if 0 <= value <= 100:
            self.ui.progressBar_3.setValue(value)
        else:
            print("Invalid value for progress bar.")