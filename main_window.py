from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem
from scipy import fft
from Musique.fft import FFTget
from ui_main_window_copy import Ui_MainWindow
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
        self.audiovisualizer.setGeometry(10, 10, 1281, 381)  # Adjust the geometry as needed

        # Initialize Spotify manager and Stream Analyzer (if needed)
        self.sp_manager = SpotifyManager()
        self.ear = Stream_Analyzer()
        
        
        

        # Connect existing sliders
        """self.ui.bass_gain.valueChanged.connect(self.update_bass_gain)
        self.ui.bass.setText(str("bass gain: " + str(self.ui.bass_gain.value() / 50.0)))
        
        self.ui.mid_gain.valueChanged.connect(self.update_mid_gain)
        self.ui.mid.setText("mid gain: " + str(self.ui.mid_gain.value() / 50.0))
        
        self.ui.high_gain.valueChanged.connect(self.update_high_gain)
        self.ui.high.setText("high gain: " + str(self.ui.high_gain.value() / 50.0))
        
        self.ui.visual_opacity_slider.valueChanged.connect(self.update_visual_opacity)
        self.ui.opacityLabel.setText("visual opacity: " + str(self.ui.visual_opacity_slider.value() / 100.0))
        
        
        self.ui.scale_slider.valueChanged.connect(self.set_scale_value)
        self.ui.scaleLabel.setText("scale: " + str(self.ui.scale_slider.value() / 100.0))
        self.ui.bar_width_slider.valueChanged.connect(self.set_bar_width_MW)
        self.ui.barwidthLabel.setText("bar width: " + str(self.ui.bar_width_slider.value() / 100.0))
        self.ui.smoothing_slider.valueChanged.connect(self.set_smoothing_value)
        self.ui.smoothLabel.setText("smoothing: " + str(self.ui.smoothing_slider.value() / 100.0))"""

        # Connect new sliders to placeholder methods
        
        self.ui.bass_gain.valueChanged.connect(lambda value: self.audiovisualizer.set_bass_gain(value / 50.0))
        self.ui.bass.setText(str("bass gain: " + str(self.ui.bass_gain.value() / 50.0)))
        
        self.ui.mid_gain.valueChanged.connect(lambda value: self.audiovisualizer.set_mid_gain(value / 50.0))
        self.ui.mid.setText("mid gain: " + str(self.ui.mid_gain.value() / 50.0))
        
        self.ui.high_gain.valueChanged.connect(lambda value: self.audiovisualizer.set_high_gain(value / 50.0))
        self.ui.high.setText("high gain: " + str(self.ui.high_gain.value() / 50.0))
        
        self.ui.visual_opacity_slider.valueChanged.connect(lambda value: self.audiovisualizer.windowOpacity(value / 1.0))
        self.ui.opacityLabel.setText("visual opacity: " + str(self.ui.visual_opacity_slider.value() / 100.0))
        
        self.ui.scale_slider.valueChanged.connect(slot=lambda value: self.ui.scale_slider.setValue(scale=value / 100.0))
        self.ui.scaleLabel.setText("scale: " + str(self.ui.scale_slider.value() / 100.0))
        
        self.ui.bar_width_slider.valueChanged.connect(lambda value: self.audiovisualizer.set_bar_width(value / 100.0))
        self.ui.barwidthLabel.setText("bar width: " + str(self.ui.bar_width_slider.value() / 100.0))
        
        self.ui.smoothing_slider.valueChanged.connect(lambda value: self.audiovisualizer.set_smoothing(value / 100.0))
        self.ui.smoothLabel.setText("smoothing: " + str(self.ui.smoothing_slider.value() / 100.0))
    
        
        
        
        self.ui.verticalSlider_23.valueChanged.connect(lambda value: self.audiovisualizer.set_param_2(value / 50.0))
        self.ui.verticalSlider_24.valueChanged.connect(lambda value: self.audiovisualizer.set_param_3(value / 50.0))
        self.ui.verticalSlider_25.valueChanged.connect(lambda value: self.audiovisualizer.set_param_4(value / 50.0))
        self.ui.verticalSlider_26.valueChanged.connect(lambda value: self.audiovisualizer.set_additional_gain_3(value / 50.0))
        self.ui.verticalSlider_27.valueChanged.connect(lambda value: self.audiovisualizer.set_additional_gain_4(value / 50.0))
        self.ui.verticalSlider_28.valueChanged.connect(lambda value: self.audiovisualizer.set_additional_gain_5(value / 50.0))
        self.ui.verticalSlider_29.valueChanged.connect(lambda value: self.audiovisualizer.set_additional_gain_6(value / 50.0))
        self.ui.verticalSlider_32.valueChanged.connect(lambda value: self.audiovisualizer.set_additional_gain_7(value / 50.0))
        self.ui.verticalSlider_33.valueChanged.connect(lambda value: self.audiovisualizer.set_additional_gain_8(value / 50.0))
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
        print("visual opacity: " + str(value / 100.0))
        
        
        
    def apply_scale(self, value):
        scale = value / 100.0
        self.audiovisualizer.set_scale(scale)
        
        self.ui.scaleLabel.setText("scale: " + str(scale))
        print(f"Scale Updated ApplyScale {value}")
        
    def set_bar_width_MW(self, value):
        bar_width = value / 100.0
        self.audiovisualizer.set_bar_width(bar_width)
        self.ui.barwidthLabel.setText("bar width: " + str(bar_width))
        print(f"Parameter 1 updated: {value}")
    
    def set_smoothing_value(self, value):
        smoothing = value / 100.0
        self.audiovisualizer.set_smoothing(smoothing)
        self.ui.smoothLabel.setText("smoothing: " + str(smoothing))
        print(f"Parameter 2 updated: {value}")
    
    def update_parameter_3(self, value):
        print(f"Parameter 3 updated: {value}")
    
    def update_parameter_4(self, value):
        print(f"Parameter 4 updated: {value}")
    
    def update_parameter_5(self, value):
        print(f"Parameter 5 updated: {value}")
    
    def update_parameter_6(self, value):
        print(f"Parameter 6 updated: {value}")
    
    def update_parameter_7(self, value):
        print(f"Parameter 7 updated: {value}")
    
    def update_parameter_8(self, value):
        print(f"Parameter 8 updated: {value}")
    
    def update_parameter_9(self, value):
        print(f"Parameter 9 updated: {value}")
    
    def update_parameter_10(self, value):
        print(f"Parameter 10 updated: {value}")
    
        
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