"""def load_ui(self):
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.textEdit_4.textChanged.connect(self.on_text_edit_change)
    self.ui.gridLayoutWidget = QWidget(self.ui.centralwidget)
    self.ui.gridLayoutWidget_11 = QWidget(self.ui.centralwidget)
    self.ui.gridLayoutWidget_9 = QWidget(self.ui.centralwidget)
    self.ui.gridLayoutWidget_15 = QWidget(self.ui.centralwidget)
    self.ui.gridLayoutWidget_7 = QWidget(self.ui.centralwidget)
    self.ui.gridLayoutWidget_10 = QWidget(self.ui.centralwidget)
    self.ui.gridLayout_14 = QGridLayout(self.ui.centralwidget)
    self.ui.gridLayout_14.addWidget(self.ui.tabWidget_3, 0, 0, 1, 1)
    self.ui.horizontalLayoutWidget = QWidget(self.ui.centralwidget)
    self.ui.horizontalLayoutWidget_7 = QWidget(self.ui.centralwidget)
    self.ui.horizontalLayoutWidget_6 = QWidget(self.ui.centralwidget)
    self.ui.horizontalLayoutWidget_8 = QWidget(self.ui.centralwidget)
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
    self.ui.opengl3dvisual_3.resizeGL(1920, 1080)

    # Initialise PartitionWidget pour le générateur d'accords

    # Autres widgets et configurations spécifiques
    # Ajoutez ici toute configuration supplémentaire nécessaire pour les autres widgets

    self.ui.pushButton_5.clicked.connect(self.on_button_click)

    self.ui.tableWidget_3.setColumnCount(1)
    self.ui.tableWidget_3.setColumnWidth(0, 450)
    self.ui.tableWidget_3.setHorizontalHeaderLabels(["Song", "Actions"])
    self.ui.tableWidget_3.setRowCount(len(self.sp_manager.get_unique_liked_songs()))

    # Configuration initiale de tableWidget_3 pour les chansons aimées
    self.ui.tabWidget_3 = QTabWidget(self.ui.centralwidget)
    # Assurez-vous que tabWidget est bien un widget et non une classe
    self.ui.tabWidget_3 = self.ui.tabWidget if hasattr(self.ui, 'tabWidget') else QTabWidget(self)

    # Initialisation des onglets

    self.ui.tabWidget_3.setTabText(0, "Musique")
    self.ui.tabWidget_3.setTabText(1, "Programmation")
    self.ui.tabWidget_3.setTabText(2, "AI")
    self.ui.tabWidget_3.setTabText(3, "Jeux")
    self.ui.tabWidget_3.setTabText(4, "Montage Video")
    self.ui.tabWidget_3.setTabText(5, "Perso")
    self.ui.tabWidget_3.font()  # Ajoutez cette ligne pour définir la police de l'onglet
    centralwidget = QWidget(self.ui.centralwidget)
    centralwidget.setLayout(self.ui.gridLayout_14)
    self.ui.tab_AI = QWidget(self.ui.tabWidget_3)  # texte de l'onglet == "AI"
    self.ui.tab_musique = QWidget(self.ui.tabWidget_3)  # texte de l'onglet == musique
    self.ui.tab_jeux = QWidget(self.ui.tabWidget_3)  # texte de l'onglet == jeux
    self.ui.tab_montage_video_3 = QWidget(self.ui.tabWidget_3)  # texte de l'onglet == montage video
    self.ui.tab_perso = QWidget(self.ui.tabWidget_3)  # texte de l'onglet == perso
    self.ui.tab_programmation = QWidget(self.ui.tabWidget_3)  # texte de l'onglet == programmation

    # Ajout des onglets
    # self.ui.tab_AI = QTabWidget(self.ui.gridLayoutWidget)
    # self.ui.tab_musique = QTabWidget(self.ui.tab_musique)

    # self.ui.tabWidget.addTab(self.ui.tab_musique_3, "Musique")
    # self.ui.tab_musique_3.setObjectName("tab_musique")
    self.ui.widget_partition = PartitionWidget()
    self.ui.widget_partition.draw_staff()
    self.ui.widget_partition.add_clef()
    # self.ui.pushButtonApply_3.clicked.connect(self.ui.widget_partition.generate)
    # self.ui.tab_programmation = QTabWidget(self.ui.tab_programmation)
    # self.ui.tabWidget.addTab(self.ui.tab_programmation_3, "Programmation")
    # self.ui.tab_AI = QTabWidget(self.ui.tab_AI)
    # self.ui.tabWidget.addTab(self.ui.tab_AI_3, "AI")
    # self.ui.tab_jeux = QTabWidget(self.ui.tab_jeux)
    # self.ui.tabWidget.addTab(self.ui.tab_jeux_3, "Jeux")
    # self.ui.tab_montage_video = QTabWidget(self.ui.tab_montage_video)
    # self.ui.tabWidget.addTab(self.ui.tab_montage_video_3, "Montage Video")
    # self.ui.tab_perso = QTabWidget(self.ui.tab_perso)
    # self.ui.tabWidget.addTab(self.ui.tab_perso_3, "Perso")
    #self.ui.tab_jeux.addTab(self.ui.tab_jeux, "Jeux")
    #self.ui.tab_montage_video.addTab(self.ui.tab_montageVideo, "Montage Video")
    #self.ui.tab_perso.addTab(self.ui.tab_perso, "Perso")
    #self.ui.tab_programmation = QTabWidget(self.ui.tab_programmation, "Programmation")"""
    """self.ui.widget_generateur_accords = QTableWidget()
    self.ui.horizontalSlider_11.valueChanged.connect(self.on_slider_value_change)
    self.populate_with_good_songs()
    self.ui.pushButtonApply_3.clicked.connect(self.generate_chords())
    self.ui.widget_generateur_accords_3 = PartitionWidget()
    self.ui.widget_generateur_accords_3.setGeometry(10, 10, 300, 200)  # Ajustez selon vos besoins
    self.ui.pushButtonApply_3.clicked.connect(PartitionWidget.draw_staff)
    self.ui.pushButtonApply_3.clicked.connect(PartitionWidget.add_clef)
    self.show()"""