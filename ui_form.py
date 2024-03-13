# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QProgressBar,
    QPushButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(19, 409, 1891, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_musique = QWidget()
        self.tab_musique.setObjectName(u"tab_musique")
        self.scrollArea_2 = QScrollArea(self.tab_musique)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, -1, 1891, 331))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1889, 329))
        self.verticalScrollBar_2 = QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setGeometry(QRect(1860, -21, 20, 331))
        self.verticalScrollBar_2.setOrientation(Qt.Vertical)
        self.widget_soundcloud = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_soundcloud.setObjectName(u"widget_soundcloud")
        self.widget_soundcloud.setGeometry(QRect(1149, -11, 691, 311))
        self.label_7 = QLabel(self.widget_soundcloud)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 20, 211, 61))
        self.label_7.setStyleSheet(u"font: 22pt \"Yellowtail\";\n"
"selection-color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.widget_playlist = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_playlist.setObjectName(u"widget_playlist")
        self.widget_playlist.setGeometry(QRect(9, 9, 1131, 311))
        self.label_6 = QLabel(self.widget_playlist)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 211, 61))
        self.label_6.setStyleSheet(u"font: 22pt \"Yellowtail\";\n"
"selection-color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.widget_generateur_accords = QWidget(self.widget_playlist)
        self.widget_generateur_accords.setObjectName(u"widget_generateur_accords")
        self.widget_generateur_accords.setGeometry(QRect(800, 10, 331, 301))
        self.verticalLayoutWidget_3 = QWidget(self.widget_generateur_accords)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-1, -1, 331, 311))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.verticalLayoutWidget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setBaseSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.widget_7)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.tableWidget = QTableWidget(self.widget_playlist)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-5, 61, 731, 241))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_musique, "")
        self.tab_programmation = QWidget()
        self.tab_programmation.setObjectName(u"tab_programmation")
        self.horizontalLayoutWidget_2 = QWidget(self.tab_programmation)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 9, 1871, 311))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_ide_realtime = QWidget(self.horizontalLayoutWidget_2)
        self.widget_ide_realtime.setObjectName(u"widget_ide_realtime")

        self.horizontalLayout_2.addWidget(self.widget_ide_realtime)

        self.widget_terminal = QWidget(self.horizontalLayoutWidget_2)
        self.widget_terminal.setObjectName(u"widget_terminal")

        self.horizontalLayout_2.addWidget(self.widget_terminal)

        self.tabWidget.addTab(self.tab_programmation, "")
        self.tab_montage_video = QWidget()
        self.tab_montage_video.setObjectName(u"tab_montage_video")
        self.gridLayoutWidget_5 = QWidget(self.tab_montage_video)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(-1, 9, 1891, 321))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_viewer_3d = QWidget(self.gridLayoutWidget_5)
        self.widget_viewer_3d.setObjectName(u"widget_viewer_3d")
        self.quickWidget = QQuickWidget(self.widget_viewer_3d)
        self.quickWidget.setObjectName(u"quickWidget")
        self.quickWidget.setGeometry(QRect(1309, 9, 571, 301))
        self.quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.openGLWidget_2 = QOpenGLWidget(self.widget_viewer_3d)
        self.openGLWidget_2.setObjectName(u"openGLWidget_2")
        self.openGLWidget_2.setGeometry(QRect(899, 9, 401, 301))
        self.widget_6 = QWidget(self.widget_viewer_3d)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(19, 29, 851, 271))

        self.gridLayout_5.addWidget(self.widget_viewer_3d, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_montage_video, "")
        self.tab_AI = QWidget()
        self.tab_AI.setObjectName(u"tab_AI")
        self.stackedWidgetAI = QStackedWidget(self.tab_AI)
        self.stackedWidgetAI.setObjectName(u"stackedWidgetAI")
        self.stackedWidgetAI.setGeometry(QRect(629, 9, 1251, 311))
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidgetAI.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidgetAI.addWidget(self.page_6)
        self.verticalLayoutWidget = QWidget(self.tab_AI)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 611, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.comboBox_4 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout.addWidget(self.comboBox_4)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.comboBox_5 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout.addWidget(self.comboBox_5)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.comboBox_6 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout.addWidget(self.comboBox_6)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.comboBox_7 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.verticalLayout.addWidget(self.comboBox_7)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.comboBox_8 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.verticalLayout.addWidget(self.comboBox_8)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.horizontalSlider = QSlider(self.tab_AI)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(130, 310, 481, 16))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_13 = QLabel(self.tab_AI)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 310, 121, 16))
        self.tabWidget.addTab(self.tab_AI, "")
        self.tab_perso = QWidget()
        self.tab_perso.setObjectName(u"tab_perso")
        self.tabWidget.addTab(self.tab_perso, "")
        self.tab_jeux = QWidget()
        self.tab_jeux.setObjectName(u"tab_jeux")
        self.tabWidget.addTab(self.tab_jeux, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 2, 1)

        self.progressBar = QProgressBar(self.gridLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 5))
        self.progressBar.setBaseSize(QSize(0, 0))
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 1891, 401))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayoutWidget_2 = QWidget(self.widget_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 281, 381))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.horizontalSlider_3 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_3)

        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)

        self.horizontalSlider_2 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_2)

        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_2.addWidget(self.label_16)

        self.horizontalSlider_4 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_4)

        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_2.addWidget(self.label_17)

        self.horizontalSlider_5 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider_5)

        self.pushButtonApply = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonApply.setObjectName(u"pushButtonApply")

        self.verticalLayout_2.addWidget(self.pushButtonApply)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.horizontalLayoutWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(1280, 0))
        self.widget_4.setBaseSize(QSize(0, 0))
        self.opengl3dvisual = QOpenGLWidget(self.widget_4)
        self.opengl3dvisual.setObjectName(u"opengl3dvisual")
        self.opengl3dvisual.setGeometry(QRect(0, 10, 1281, 381))
        self.opengl3dvisual.setMinimumSize(QSize(621, 0))

        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.horizontalLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")

        self.horizontalLayout.addWidget(self.widget_3)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(270, 810, 1249, 262))
        self.gridLayoutWidget_2 = QWidget(self.widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(9, -1, 421, 241))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_2.addWidget(self.comboBox_3, 5, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_2.addWidget(self.comboBox_2, 3, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 7, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.widget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(1090, 180, 160, 80))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber = QLCDNumber(self.gridLayoutWidget_3)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_3.addWidget(self.lcdNumber, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(449, 9, 631, 251))
        self.horizontalLayoutWidget_3 = QWidget(self.widget_8)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(9, -1, 621, 251))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalSlider_11 = QSlider(self.horizontalLayoutWidget_3)
        self.verticalSlider_11.setObjectName(u"verticalSlider_11")
        self.verticalSlider_11.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.verticalSlider_11)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalSlider_10 = QSlider(self.horizontalLayoutWidget_3)
        self.verticalSlider_10.setObjectName(u"verticalSlider_10")
        self.verticalSlider_10.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.verticalSlider_10)

        self.gridLayoutWidget_4 = QWidget(Form)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(19, 819, 254, 241))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_9 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_9.setObjectName(u"verticalSlider_9")
        self.verticalSlider_9.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_9, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider, 0, 0, 1, 1)

        self.verticalSlider_2 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_2, 0, 8, 1, 1)

        self.verticalSlider_4 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_4, 0, 6, 1, 1)

        self.verticalSlider_8 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_8, 0, 2, 1, 1)

        self.verticalSlider_5 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_5, 0, 5, 1, 1)

        self.verticalSlider_3 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_3, 0, 7, 1, 1)

        self.verticalSlider_6 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_6, 0, 4, 1, 1)

        self.verticalSlider_7 = QSlider(self.gridLayoutWidget_4)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_7, 0, 3, 1, 1)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(1550, 820, 351, 251))
        self.openGLWidget = QOpenGLWidget(self.widget_5)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(0, 0, 351, 251))

        self.retranslateUi(Form)
        self.verticalScrollBar_2.sliderMoved.connect(self.scrollArea_2.update)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Soundcloud Player", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Playlist automatis\u00e9e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_musique), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_programmation), QCoreApplication.translate("Form", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_montage_video), QCoreApplication.translate("Form", u"Page", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Slider", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_AI), QCoreApplication.translate("Form", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_perso), QCoreApplication.translate("Form", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_jeux), QCoreApplication.translate("Form", u"Page", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButtonApply.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

