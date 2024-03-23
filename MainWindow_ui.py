# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

from qopenglbarwidget import QOpenGLBarWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(1, 1, 1891, 401))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.horizontalLayoutWidget)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayoutWidget_5 = QWidget(self.widget_12)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 1492, 13004))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.verticalLayoutWidget_5)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_5.addWidget(self.label_33)

        self.horizontalSlider_11 = QSlider(self.verticalLayoutWidget_5)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        self.horizontalSlider_11.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_11)

        self.label_34 = QLabel(self.verticalLayoutWidget_5)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_5.addWidget(self.label_34)

        self.horizontalSlider_12 = QSlider(self.verticalLayoutWidget_5)
        self.horizontalSlider_12.setObjectName(u"horizontalSlider_12")
        self.horizontalSlider_12.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_12)

        self.label_35 = QLabel(self.verticalLayoutWidget_5)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_5.addWidget(self.label_35)

        self.horizontalSlider_13 = QSlider(self.verticalLayoutWidget_5)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_13)

        self.label_36 = QLabel(self.verticalLayoutWidget_5)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_5.addWidget(self.label_36)

        self.horizontalSlider_14 = QSlider(self.verticalLayoutWidget_5)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_14)

        self.pushButtonApply_3 = QPushButton(self.verticalLayoutWidget_5)
        self.pushButtonApply_3.setObjectName(u"pushButtonApply_3")

        self.verticalLayout_5.addWidget(self.pushButtonApply_3)

        self.horizontalSlider_11.raise_()
        self.label_36.raise_()
        self.pushButtonApply_3.raise_()
        self.horizontalSlider_13.raise_()
        self.label_34.raise_()
        self.horizontalSlider_12.raise_()
        self.horizontalSlider_14.raise_()
        self.label_33.raise_()
        self.label_35.raise_()

        self.horizontalLayout_7.addWidget(self.widget_12)

        self.widget_15 = QWidget(self.horizontalLayoutWidget)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(1280, 0))
        self.widget_15.setBaseSize(QSize(0, 0))
        self.opengl3dvisual_3 = QOpenGLBarWidget(self.widget_15)
        self.opengl3dvisual_3.setObjectName(u"opengl3dvisual_3")
        self.opengl3dvisual_3.setGeometry(QRect(0, 10, 1281, 381))
        self.opengl3dvisual_3.setMinimumSize(QSize(621, 0))

        self.horizontalLayout_7.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.horizontalLayoutWidget)
        self.widget_16.setObjectName(u"widget_16")

        self.horizontalLayout_7.addWidget(self.widget_16)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(251, 801, 1249, 262))
        self.gridLayoutWidget_7 = QWidget(self.widget)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(9, -1, 2898, 10428))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.gridLayoutWidget_7)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_11.addWidget(self.label_37, 2, 0, 1, 1)

        self.comboBox_17 = QComboBox(self.gridLayoutWidget_7)
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.gridLayout_11.addWidget(self.comboBox_17, 5, 0, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_7)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_11.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_7)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_11.addWidget(self.label_39, 4, 0, 1, 1)

        self.comboBox_18 = QComboBox(self.gridLayoutWidget_7)
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.gridLayout_11.addWidget(self.comboBox_18, 3, 0, 1, 1)

        self.comboBox_19 = QComboBox(self.gridLayoutWidget_7)
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.gridLayout_11.addWidget(self.comboBox_19, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_7)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_11.addWidget(self.pushButton_5, 7, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_7)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_11.addWidget(self.label_40, 6, 0, 1, 1)

        self.comboBox_19.raise_()
        self.comboBox_18.raise_()
        self.comboBox_17.raise_()
        self.label_39.raise_()
        self.label_37.raise_()
        self.pushButton_5.raise_()
        self.label_38.raise_()
        self.label_40.raise_()
        self.gridLayoutWidget_9 = QWidget(self.widget)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(1090, 180, 160, 80))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lcdNumber_3 = QLCDNumber(self.gridLayoutWidget_9)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.gridLayout_12.addWidget(self.lcdNumber_3, 0, 0, 1, 1)

        self.widget_17 = QWidget(self.widget)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(449, 9, 631, 251))
        self.horizontalLayoutWidget_6 = QWidget(self.widget_17)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(9, -1, 6086, 5172))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.textEdit_3 = QTextEdit(self.horizontalLayoutWidget_6)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.horizontalLayout_8.addWidget(self.textEdit_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_8.addItem(self.verticalSpacer_5)

        self.verticalSlider_23 = QSlider(self.horizontalLayoutWidget_6)
        self.verticalSlider_23.setObjectName(u"verticalSlider_23")
        self.verticalSlider_23.setOrientation(Qt.Vertical)

        self.horizontalLayout_8.addWidget(self.verticalSlider_23)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_8.addItem(self.verticalSpacer_6)

        self.verticalSlider_24 = QSlider(self.horizontalLayoutWidget_6)
        self.verticalSlider_24.setObjectName(u"verticalSlider_24")
        self.verticalSlider_24.setOrientation(Qt.Vertical)

        self.horizontalLayout_8.addWidget(self.verticalSlider_24)

        self.gridLayoutWidget_10 = QWidget(self.centralwidget)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(0, 810, 13460, 241))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_28 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_28.setObjectName(u"verticalSlider_28")
        self.verticalSlider_28.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_28, 0, 6, 1, 1)

        self.verticalSlider_30 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_30.setObjectName(u"verticalSlider_30")
        self.verticalSlider_30.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_30, 0, 5, 1, 1)

        self.verticalSlider_31 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_31.setObjectName(u"verticalSlider_31")
        self.verticalSlider_31.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_31, 0, 7, 1, 1)

        self.verticalSlider_32 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_32.setObjectName(u"verticalSlider_32")
        self.verticalSlider_32.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_32, 0, 4, 1, 1)

        self.verticalSlider_29 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_29.setObjectName(u"verticalSlider_29")
        self.verticalSlider_29.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_29, 0, 2, 1, 1)

        self.verticalSlider_33 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_33.setObjectName(u"verticalSlider_33")
        self.verticalSlider_33.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_33, 0, 3, 1, 1)

        self.verticalSlider_26 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_26.setObjectName(u"verticalSlider_26")
        self.verticalSlider_26.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_26, 0, 0, 1, 1)

        self.verticalSlider_27 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_27.setObjectName(u"verticalSlider_27")
        self.verticalSlider_27.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_27, 0, 8, 1, 1)

        self.verticalSlider_25 = QSlider(self.gridLayoutWidget_10)
        self.verticalSlider_25.setObjectName(u"verticalSlider_25")
        self.verticalSlider_25.setOrientation(Qt.Vertical)

        self.gridLayout_13.addWidget(self.verticalSlider_25, 0, 1, 1, 1)

        self.verticalSlider_25.raise_()
        self.verticalSlider_27.raise_()
        self.verticalSlider_33.raise_()
        self.verticalSlider_26.raise_()
        self.verticalSlider_31.raise_()
        self.verticalSlider_32.raise_()
        self.verticalSlider_28.raise_()
        self.verticalSlider_30.raise_()
        self.verticalSlider_29.raise_()
        self.widget_18 = QWidget(self.centralwidget)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(1531, 811, 351, 251))
        self.openGLWidget_5 = QOpenGLWidget(self.widget_18)
        self.openGLWidget_5.setObjectName(u"openGLWidget_5")
        self.openGLWidget_5.setGeometry(QRect(0, 0, 351, 251))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 400, 1891, 2579))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.progressBar_3 = QProgressBar(self.gridLayoutWidget)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMinimumSize(QSize(0, 5))
        self.progressBar_3.setBaseSize(QSize(0, 0))
        self.progressBar_3.setValue(24)

        self.gridLayout_14.addWidget(self.progressBar_3, 0, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.gridLayoutWidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_musique_3 = QWidget()
        self.tab_musique_3.setObjectName(u"tab_musique_3")
        self.scrollArea_4 = QScrollArea(self.tab_musique_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(-1, -1, 1891, 331))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1889, 329))
        self.verticalScrollBar_4 = QScrollBar(self.scrollAreaWidgetContents_4)
        self.verticalScrollBar_4.setObjectName(u"verticalScrollBar_4")
        self.verticalScrollBar_4.setGeometry(QRect(1860, -21, 20, 331))
        self.verticalScrollBar_4.setOrientation(Qt.Vertical)
        self.widget_soundcloud_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_soundcloud_3.setObjectName(u"widget_soundcloud_3")
        self.widget_soundcloud_3.setGeometry(QRect(1149, -11, 691, 311))
        self.label_41 = QLabel(self.widget_soundcloud_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 20, 211, 61))
        self.label_41.setStyleSheet(u"font: 22pt \"Yellowtail\";\n"
"selection-color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.webEngineView = QWebEngineView(self.widget_soundcloud_3)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(0, 80, 681, 231))
        self.webEngineView.setProperty("url", QUrl(u"about:blank"))
        self.widget_playlist_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_playlist_3.setObjectName(u"widget_playlist_3")
        self.widget_playlist_3.setGeometry(QRect(9, 9, 801, 311))
        self.label_42 = QLabel(self.widget_playlist_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 0, 211, 61))
        self.label_42.setStyleSheet(u"font: 22pt \"Yellowtail\";\n"
"selection-color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"")
        self.widget_generateur_accords_3 = QWidget(self.widget_playlist_3)
        self.widget_generateur_accords_3.setObjectName(u"widget_generateur_accords_3")
        self.widget_generateur_accords_3.setGeometry(QRect(800, 10, 331, 301))
        self.widget_19 = QWidget(self.widget_generateur_accords_3)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(19, 9, 291, 231))
        self.pushButton_generate_chords_3 = QPushButton(self.widget_generateur_accords_3)
        self.pushButton_generate_chords_3.setObjectName(u"pushButton_generate_chords_3")
        self.pushButton_generate_chords_3.setGeometry(QRect(30, 260, 271, 31))
        self.tableWidget_3 = QTableWidget(self.widget_playlist_3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(-5, 61, 731, 241))
        self.widget_generateur_accords_3.raise_()
        self.label_42.raise_()
        self.tableWidget_3.raise_()
        self.widget_partition = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_partition.setObjectName(u"widget_partition")
        self.widget_partition.setGeometry(QRect(740, 10, 401, 621))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.widget_soundcloud_3.raise_()
        self.widget_playlist_3.raise_()
        self.verticalScrollBar_4.raise_()
        self.widget_partition.raise_()
        self.horizontalLayoutWidget_8 = QWidget(self.tab_musique_3)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(-1, 339, 1891, 251))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.horizontalLayoutWidget_8)
        self.widget_21.setObjectName(u"widget_21")
        self.textEdit_4 = QTextEdit(self.widget_21)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(0, 0, 1691, 271))

        self.horizontalLayout_10.addWidget(self.widget_21)

        self.verticalSlider_40 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_40.setObjectName(u"verticalSlider_40")
        self.verticalSlider_40.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_40)

        self.verticalSlider_39 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_39.setObjectName(u"verticalSlider_39")
        self.verticalSlider_39.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_39)

        self.verticalSlider_38 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_38.setObjectName(u"verticalSlider_38")
        self.verticalSlider_38.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_38)

        self.verticalSlider_37 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_37.setObjectName(u"verticalSlider_37")
        self.verticalSlider_37.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_37)

        self.verticalSlider_36 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_36.setObjectName(u"verticalSlider_36")
        self.verticalSlider_36.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_36)

        self.verticalSlider_35 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_35.setObjectName(u"verticalSlider_35")
        self.verticalSlider_35.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_35)

        self.verticalSlider_34 = QSlider(self.horizontalLayoutWidget_8)
        self.verticalSlider_34.setObjectName(u"verticalSlider_34")
        self.verticalSlider_34.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.verticalSlider_34)

        self.tabWidget_3.addTab(self.tab_musique_3, "")
        self.tab_programmation_3 = QWidget()
        self.tab_programmation_3.setObjectName(u"tab_programmation_3")
        self.horizontalLayoutWidget_7 = QWidget(self.tab_programmation_3)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(9, 9, 1871, 311))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_ide_realtime_3 = QWidget(self.horizontalLayoutWidget_7)
        self.widget_ide_realtime_3.setObjectName(u"widget_ide_realtime_3")

        self.horizontalLayout_9.addWidget(self.widget_ide_realtime_3)

        self.widget_terminal_3 = QWidget(self.horizontalLayoutWidget_7)
        self.widget_terminal_3.setObjectName(u"widget_terminal_3")

        self.horizontalLayout_9.addWidget(self.widget_terminal_3)

        self.tabWidget_3.addTab(self.tab_programmation_3, "")
        self.tab_montage_video_3 = QWidget()
        self.tab_montage_video_3.setObjectName(u"tab_montage_video_3")
        self.gridLayoutWidget_11 = QWidget(self.tab_montage_video_3)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(-1, 9, 1891, 321))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_viewer_3d_3 = QWidget(self.gridLayoutWidget_11)
        self.widget_viewer_3d_3.setObjectName(u"widget_viewer_3d_3")
        self.quickWidget_3 = QQuickWidget(self.widget_viewer_3d_3)
        self.quickWidget_3.setObjectName(u"quickWidget_3")
        self.quickWidget_3.setGeometry(QRect(1309, 9, 571, 301))
        self.quickWidget_3.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.openGLWidget_6 = QOpenGLWidget(self.widget_viewer_3d_3)
        self.openGLWidget_6.setObjectName(u"openGLWidget_6")
        self.openGLWidget_6.setGeometry(QRect(899, 9, 401, 301))
        self.widget_20 = QWidget(self.widget_viewer_3d_3)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(19, 29, 851, 271))

        self.gridLayout_15.addWidget(self.widget_viewer_3d_3, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_montage_video_3, "")
        self.tab_AI_3 = QWidget()
        self.tab_AI_3.setObjectName(u"tab_AI_3")
        self.stackedWidgetAI_3 = QStackedWidget(self.tab_AI_3)
        self.stackedWidgetAI_3.setObjectName(u"stackedWidgetAI_3")
        self.stackedWidgetAI_3.setGeometry(QRect(629, 9, 1251, 311))
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.stackedWidgetAI_3.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.stackedWidgetAI_3.addWidget(self.page_10)
        self.verticalLayoutWidget_6 = QWidget(self.tab_AI_3)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 1510, 15612))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.verticalLayoutWidget_6)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_6.addWidget(self.label_43)

        self.comboBox_20 = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.verticalLayout_6.addWidget(self.comboBox_20)

        self.label_44 = QLabel(self.verticalLayoutWidget_6)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_6.addWidget(self.label_44)

        self.comboBox_21 = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_21.setObjectName(u"comboBox_21")

        self.verticalLayout_6.addWidget(self.comboBox_21)

        self.label_45 = QLabel(self.verticalLayoutWidget_6)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_6.addWidget(self.label_45)

        self.comboBox_22 = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_22.setObjectName(u"comboBox_22")

        self.verticalLayout_6.addWidget(self.comboBox_22)

        self.label_46 = QLabel(self.verticalLayoutWidget_6)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_6.addWidget(self.label_46)

        self.comboBox_23 = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_23.setObjectName(u"comboBox_23")

        self.verticalLayout_6.addWidget(self.comboBox_23)

        self.label_47 = QLabel(self.verticalLayoutWidget_6)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_6.addWidget(self.label_47)

        self.comboBox_24 = QComboBox(self.verticalLayoutWidget_6)
        self.comboBox_24.setObjectName(u"comboBox_24")

        self.verticalLayout_6.addWidget(self.comboBox_24)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_6.addWidget(self.pushButton_6)

        self.horizontalSlider_15 = QSlider(self.tab_AI_3)
        self.horizontalSlider_15.setObjectName(u"horizontalSlider_15")
        self.horizontalSlider_15.setGeometry(QRect(130, 310, 481, 16))
        self.horizontalSlider_15.setOrientation(Qt.Horizontal)
        self.label_48 = QLabel(self.tab_AI_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(0, 310, 121, 16))
        self.tabWidget_3.addTab(self.tab_AI_3, "")
        self.tab_perso_3 = QWidget()
        self.tab_perso_3.setObjectName(u"tab_perso_3")
        self.tabWidget_3.addTab(self.tab_perso_3, "")
        self.tab_jeux_3 = QWidget()
        self.tab_jeux_3.setObjectName(u"tab_jeux_3")
        self.tabWidget_3.addTab(self.tab_jeux_3, "")

        self.gridLayout_14.addWidget(self.tabWidget_3, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButtonApply_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Soundcloud Player", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Playlist automatis\u00e9e", None))
        self.pushButton_generate_chords_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_musique_3), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_programmation_3), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_montage_video_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Slider", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_AI_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_perso_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_jeux_3), QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi

