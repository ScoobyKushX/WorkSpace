import PySide6.QtWidgets, PySide6.QtGui, PySide6.QtCore, PySide6.QtUiTools
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from ui_main_window import Ui_MainWindow
from spotify_manager import SpotifyManager
from Chords_generator import PartitionWidget


#from audio_visual import RealTimeAudioVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.sp_manager = SpotifyManager()  # Initialise SpotifyManager
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connecte le bouton à la fonction on_button_click
        self.ui.pushButton_5.clicked.connect(self.on_button_click)
        self.ui.pushButtonApply_3.clicked.connect(self.generate_chords)

        # Configuration initiale de tableWidget_3 pour les chansons aimées
        self.ui.tableWidget_3.setColumnCount(1)
        self.ui.tableWidget_3.setColumnWidth(0, 450)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["Song"])
        self.ui.tableWidget_3.setRowCount(len(self.sp_manager.get_unique_liked_songs()))

        # Connecte les sliders à leurs événements
        self.ui.horizontalSlider_11.valueChanged.connect(self.on_slider_value_change)
        self.ui.horizontalSlider_12.valueChanged.connect(self.on_slider_value_change)
        self.ui.horizontalSlider_13.valueChanged.connect(self.on_slider_value_change)
        self.ui.horizontalSlider_14.valueChanged.connect(self.on_slider_value_change)

        # Connecte le QOpenGLWidget
        self.ui.opengl3dvisual_3.initializeGL()
        self.ui.opengl3dvisual_3.paintGL()
        self.ui.opengl3dvisual_3.resizeGL()

        # Initialise PartitionWidget pour le générateur d'accords

        # Autres widgets et configurations spécifiques
        # Ajoutez ici toute configuration supplémentaire nécessaire pour les autres widgets

        self.ui.pushButton_5.clicked.connect(self.on_button_click)

        self.ui.tableWidget_3.setColumnCount(1)
        self.ui.tableWidget_3.setColumnWidth(0, 450)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["Song", "Actions"])
        self.ui.tableWidget_3.setRowCount(len(self.sp_manager.get_unique_liked_songs()))

        # Assurez-vous que tabWidget est bien un widget et non une classe
        self.ui.tabWidget = self.ui.tabWidget if hasattr(self.ui, 'tabWidget') else QTabWidget(self)

        # Initialisation des onglets
        self.ui.tabWidget = QTabWidget(self.ui.centralwidget)
        self.ui.tabWidget.setTabText("Musique")
        self.ui.tabWidget.setTabText("Programmation")
        self.ui.tabWidget.setTabText("AI")
        self.ui.tabWidget.setTabText("Jeux")
        self.ui.tabWidget.setTabText("Montage Video")
        self.ui.tabWidget.setTabText("Perso")
        self.ui.tabWidget.font() # Ajoutez cette ligne pour définir la police de l'onglet

        self.ui.tab_AI = QWidget(self.ui.tabWidget)
        self.ui.tab_musique = QWidget(self.ui.tabWidget)
        self.ui.tab_jeux = QWidget(self.ui.tabWidget)
        self.ui.tab_montage_video_3 = QWidget(self.ui.tabWidget)
        self.ui.tab_perso = QWidget(self.ui.tabWidget)
        self.ui.tab_programmation = QWidget(self.ui.tabWidget)

        # Ajout des onglets
        #self.ui.tab_AI = QTabWidget(self.ui.gridLayoutWidget)
        #self.ui.tab_musique = QTabWidget(self.ui.tab_musique)

        self.ui.tabWidget.addTab(self.ui.tab_musique_3, "Musique")
        self.ui.tab_musique_3.setObjectName("tab_musique")
        self.ui.widget_partition = PartitionWidget()
        self.ui.widget_partition.draw_staff()
        self.ui.widget_partition.add_clef()
        #self.ui.pushButtonApply_3.clicked.connect(self.ui.widget_partition.generate)
        #self.ui.tab_programmation = QTabWidget(self.ui.tab_programmation)
        self.ui.tabWidget.addTab(self.ui.tab_programmation_3, "Programmation")
        #self.ui.tab_AI = QTabWidget(self.ui.tab_AI)
        self.ui.tabWidget.addTab(self.ui.tab_AI_3, "AI")
        #self.ui.tab_jeux = QTabWidget(self.ui.tab_jeux)
        self.ui.tabWidget.addTab(self.ui.tab_jeux_3, "Jeux")
        #self.ui.tab_montage_video = QTabWidget(self.ui.tab_montage_video)
        self.ui.tabWidget.addTab(self.ui.tab_montage_video_3, "Montage Video")
        #self.ui.tab_perso = QTabWidget(self.ui.tab_perso)
        self.ui.tabWidget.addTab(self.ui.tab_perso_3, "Perso")
        """self.ui.tab_jeux.addTab(self.ui.tab_jeux, "Jeux")
        self.ui.tab_montage_video.addTab(self.ui.tab_montageVideo, "Montage Video")
        self.ui.tab_perso.addTab(self.ui.tab_perso, "Perso")
        self.ui.tab_programmation = QTabWidget(self.ui.tab_programmation, "Programmation")"""
        self.ui.widget_generateur_accords = QTableWidget()
        self.ui.horizontalSlider_11.valueChanged.connect(self.on_slider_value_change)
        self.populate_with_good_songs()
        self.ui.pushButtonApply_3.clicked.connect(self.generate_chords())
        self.ui.widget_generateur_accords_3 = PartitionWidget()
        self.ui.widget_generateur_accords_3.setGeometry(10, 10, 300, 200)  # Ajustez selon vos besoins
        self.ui.pushButtonApply_3.clicked.connect("generate", PartitionWidget.draw_staff, PartitionWidget.add_clef)

        self.show()

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

    def generate_chords(self):
        print("generate_chords clicked!")

