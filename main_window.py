from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from ui_main_window import Ui_MainWindow
from spotify_manager import SpotifyManager
from Chords_generator import PartitionWidget

# from audio_visual import RealTimeAudioVisualizer

class MainWindow(QMainWindow):
    def __init__(self, parent=Ui_MainWindow):
        super(MainWindow, self).__init__(parent=None)
        self.sp_manager = SpotifyManager()  # Initialise SpotifyManager
        self.ui = Ui_MainWindow()  # Create an instance of the user interface
        self.ui.setupUI(self)  # Load the user interface
        self.populate_playlist_table()
        self.ui.gridLayout_14.addWidget(self.ui.tabWidget_3, 0, 0, 1, 1)
        self.ui.gridLayout_14.addWidget(self.ui.progressBar_3, 1, 0, 1, 1)
        self.ui.progressBar_3.setMaximum(100)

    def on_button_click(self):
        try:
            selected_music = self.ui.tableWidget_3.item(self.ui.tableWidget_3.currentRow(), 0).text()
            print(f"Playing: {selected_music}")
        except AttributeError:
            print("No music selected. Please select a music from the table.")

    def on_text_edit_change(self):
        print("Text changed!")

    def on_slider_value_change(self, value):
        print(f"Slider value changed: {value}")

    def populate_playlist_table(self):
        top_tracks = self.sp_manager.get_unique_liked_songs()
        recently_played_tracks = self.sp_manager.get_recently_played_tracks()

        if top_tracks is None or recently_played_tracks is None:
            print("Une des listes de pistes est vide.")
            return

        
        
        self.ui.tableWidget_3.setRowCount(len(top_tracks and recently_played_tracks))
        self.ui.tableWidget_3.setColumnCount(1)
        self.ui.tableWidget_3.setColumnWidth(1, 900)

        for i, track in enumerate(top_tracks and recently_played_tracks):
            if 'name' in track:
                track_name = QTableWidgetItem(track['name'])
            else:
                track_name = QTableWidgetItem("Nom de la piste indisponible")

            self.ui.tableWidget_3.setItem(i, 1, track_name)
                    
    def generate_chords(self):
        print("generate_chords clicked!")

    def update_progress_bar(self, value):
        if 0 <= value <= 100:
            self.ui.progressBar_3.setValue(value)
        else:
            print("Invalid value for progress bar.")
