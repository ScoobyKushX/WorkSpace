from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from scipy import fft
from Musique.fft import FFTget
from ui_main_window import Ui_MainWindow
from Musique.spotify_manager import SpotifyManager
from audio_visual import OpenGLBarWidget
from Musique.StreamAnalyzer import Stream_Analyzer
from PySide6.QtCore import Qt, QTimer, QTime
import subprocess

class MainWindowClass(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowClass, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize the audio visualizer
        self.audiovisualizer = OpenGLBarWidget(self.ui.opengl3dvisual_3)  # Ensure to add an OpenGLWidget in Qt Designer and name it 'opengl_widget'
        self.audiovisualizer.setGeometry(10, 10, 400, 300)  # Adjust the geometry as needed

        # Initialize Spotify manager and Stream Analyzer (if needed)
        self.sp_manager = SpotifyManager()
        self.ear = Stream_Analyzer()
        
        
        

        # Connect existing sliders
        self.ui.horizontalSlider_11.valueChanged.connect(self.update_bass_gain)
        self.ui.horizontalSlider_12.valueChanged.connect(self.update_mid_gain)
        self.ui.horizontalSlider_13.valueChanged.connect(self.update_high_gain)
        self.ui.horizontalSlider_14.valueChanged.connect(self.update_visual_opacity)
        self.ui.horizontalSlider_15.valueChanged.connect(self.update_parameter_1)
        self.ui.verticalSlider_38.valueChanged.connect(self.update_parameter_2)
        self.ui.verticalSlider_39.valueChanged.connect(self.audiovisualizer.set_scale)
        self.ui.verticalSlider_40.valueChanged.connect(self.audiovisualizer.set_bar_width)

        # Connect new sliders to placeholder methods
        self.ui.verticalSlider_37.valueChanged.connect(self.update_parameter_0)
        self.ui.verticalSlider_36.valueChanged.connect(self.update_parameter_2)
        self.ui.verticalSlider_35.valueChanged.connect(self.update_parameter_3)
        self.ui.verticalSlider_34.valueChanged.connect(self.update_parameter_4)
        
        # Populate playlist, connect signals, etc.
        self.populate_playlist_table()
        self.ui.tableWidget_3.itemSelectionChanged.connect(self.play_selected_track)

    def update_bass_gain(self, value):
        self.audiovisualizer.set_bass_gain(value / 50.0)  # Adjust the divisor as needed

    def update_mid_gain(self, value):
        self.audiovisualizer.set_mid_gain(value / 50.0)

    def update_high_gain(self, value):
        self.audiovisualizer.set_high_gain(value / 50.0)

    def update_visual_opacity(self, value):
        self.audiovisualizer.set_visual_opacity(value / 100.0)
        
        
        
    def update_parameter_0(self, value):
        print(f"Parameter 0 updated: {value}")
        
    def update_parameter_1(self, value):
        print(f"Parameter 1 updated: {value}")
    
    def update_parameter_2(self, value):
        print(f"Parameter 2 updated: {value}")
    
    def update_parameter_3(self, value):
        print(f"Parameter 3 updated: {value}")
    
    def update_parameter_4(self, value):
        print(f"Parameter 4 updated: {value}")
    
    def update_parameter_5(self, value):
        print(f"Parameter 5 updated: {value}")
    
    
        
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
            track_name.setData(Qt.ItemDataRole.UserRole, track['id'])  # Store the track ID
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
                selected_track_id = selected_track_item.data(Qt.ItemDataRole.UserRole)

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
        self.timer = QTimer(self)
        self.ear = Stream_Analyzer()
        self.ear.stream.start()
        self.timer.timeout.connect(self.init_visualizer_update)
        self.timer.start(self.ear.update)