from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from ui_main_window import Ui_MainWindow
from Musique.spotify_manager import SpotifyManager
from audio_visual import OpenGLBarWidget
from Musique.StreamAnalyzer import Stream_Analyzer

class MainWindowClass(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowClass, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUI(self)
        self.ui.opengl3dvisual_3 = OpenGLBarWidget(self)
        self.ui.horizontalLayout_7.addWidget(self.ui.opengl3dvisual_3)  # Replace 'someLayout' with the actual layout name
        self.sp_manager = SpotifyManager()
        self.ear = Stream_Analyzer()
        # Other initializations and method definitions...

        self.sp_manager = SpotifyManager()

        # Populate playlist, connect signals, etc.
        self.populate_playlist_table()


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
        unique_tracks = self.sp_manager.get_unique_liked_songs()
        self.ui.tableWidget_3.setRowCount(len(unique_tracks))
        self.ui.tableWidget_3.setColumnCount(3)  # If you have three columns as mentioned earlier

        for i, track in enumerate(unique_tracks):
            row = i // 3
            column = i % 3
            track_name = QTableWidgetItem(track['name'] if 'name' in track else 'Unknown Name')
            track_name.setData(Qt.UserRole, track['id'])  # Store the track ID
            self.ui.tableWidget_3.setItem(row, column, track_name)

        # Adjust the width of the columns if necessary
        for i in range(3):
            self.ui.tableWidget_3.setColumnWidth(i, 220)  # Adjust width as needed

    def play_selected_track(self):
        try:
            selected_row = self.ui.tableWidget_3.currentRow()
            selected_column = self.ui.tableWidget_3.currentColumn()  # Obtenez la colonne sélectionnée
            selected_track_item = self.ui.tableWidget_3.item(selected_row, selected_column)

            if selected_track_item is not None:
                selected_track_id = selected_track_item.data(Qt.UserRole)

                if selected_track_id:
                    # Arrête la musique en cours avant de jouer la nouvelle sélection (si nécessaire)
                    # self.sp_manager.stop_music()  # Décommentez si vous avez implémenté stop_music
                    self.sp_manager.play_music(track_id=selected_track_id)
                else:
                    print("No track ID selected.")
            else:
                print("No track selected.")
        except Exception as e:
            print(f"Error while attempting to play the track: {e}")

    def launch_spotify(self):
        try:
            subprocess.Popen(["spotify"])
        except Exception as e:
            print(f"Error launching Spotify: {e}")

    def init_visualizer_update(self):
        self.ui.opengl3dvisual_3.timer = QTimer(self)
        self.ear = Stream_Analyzer()
        self.ear.start()
        self.timer.timeout.connect(self.init_visualizer_update)
        self.timer.start(self.ear.updates_per_second, 1000)