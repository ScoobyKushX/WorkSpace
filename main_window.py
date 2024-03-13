import PySide6
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from ui_form import Ui_Form
from spotify_manager import SpotifyManager


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.sp_manager = SpotifyManager()  # Initialise SpotifyManager
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()
        self.ui.pushButton.clicked.connect(self.on_button_click)

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Song", "Actions"])
        self.ui.tableWidget.setRowCount(len(self.sp_manager.get_unique_liked_songs()))

        # Assurez-vous que tabWidget est bien un widget et non une classe
        self.ui.tabWidget = self.ui.tabWidget if hasattr(self.ui, 'tabWidget') else QTabWidget(self)

        # Initialisation des onglets
        self.ui.tab_AI = QWidget()
        self.ui.tab_musique = QWidget()
        self.ui.tab_jeux = QWidget()
        self.ui.tab_montageVideo = QWidget()
        self.ui.tab_perso = QWidget()
        self.ui.tab_programmation = QWidget()

        # Ajout des onglets
        self.ui.tabWidget.addTab(self.ui.tab_AI, "Artificial Intelligence")
        self.ui.tabWidget.addTab(self.ui.tab_musique, "Musique")
        self.ui.tabWidget.addTab(self.ui.tab_jeux, "Jeux")
        self.ui.tabWidget.addTab(self.ui.tab_montageVideo, "Montage Video")
        self.ui.tabWidget.addTab(self.ui.tab_perso, "Perso")
        self.ui.tabWidget.addTab(self.ui.tab_programmation, "Programmation")
        self.ui.widget_generateur_accords = QTableWidget()
        self.ui.horizontalSlider.valueChanged.connect(self.on_slider_value_change)
        self.populate_with_good_songs()
        self.ui.pushButton_generate_chords.clicked.connect(self.generate_chord)
        self.show()

    def on_button_click(self):
        print("Button clicked!")

    # Cette fonction semble être référencée mais n'est pas définie.
    # Définissons-la pour éviter les erreurs.
    def on_text_edit_change(self):
        print("Text changed!")

    def on_slider_value_change(self, value):
        print(f"Slider value changed: {value}")

    def populate_with_good_songs(self):
        try:
            unique_song_ids = self.sp_manager.get_unique_liked_songs()
            self.ui.tableWidget.setRowCount(len(unique_song_ids))

            for i, track_id in enumerate(unique_song_ids):
                try:
                    track_details = self.sp_manager.sp.track(track_id)
                    track_name = f"{track_details['artists'][0]['name']} - {track_details['name']}"
                    self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(track_name))
                except Exception as e_inner:
                    print(f"Error loading song details for track ID {track_id}: {str(e_inner)}")
                    QMessageBox.critical(self, "Error",
                                         f"Failed to load song details for track ID {track_id}: {str(e_inner)}")
        except Exception as e:
            print(f"Failed to load liked songs: {str(e)}")
            QMessageBox.critical(self, "Error", f"Failed to load liked songs: {str(e)}")

