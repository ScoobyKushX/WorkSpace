# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumSize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, -1, 1920, 1080))
        self.tabWidget.setObjectName("tabWidget")
        self.musique = QtWidgets.QWidget()
        self.musique.setObjectName("musique")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.musique)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 831, 1011))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=self.musique)
        self.pushButton.setGeometry(QtCore.QRect(870, 500, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.musique)
        self.plainTextEdit.setGeometry(QtCore.QRect(1060, 20, 851, 301))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.musique)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(1060, 350, 851, 301))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=self.musique)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(1060, 680, 851, 301))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.widget = QtWidgets.QWidget(parent=self.musique)
        self.widget.setGeometry(QtCore.QRect(880, 19, 120, 451))
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(parent=self.musique)
        self.widget_2.setGeometry(QtCore.QRect(880, 560, 120, 431))
        self.widget_2.setObjectName("widget_2")
        self.tabWidget.addTab(self.musique, "")
        self.programmation = QtWidgets.QWidget()
        self.programmation.setObjectName("programmation")
        self.tabWidget.addTab(self.programmation, "")
        self.AI = QtWidgets.QWidget()
        self.AI.setObjectName("AI")
        self.tabWidget.addTab(self.AI, "")
        self.MontageVideo = QtWidgets.QWidget()
        self.MontageVideo.setObjectName("MontageVideo")
        self.tabWidget.addTab(self.MontageVideo, "")
        self.perso = QtWidgets.QWidget()
        self.perso.setObjectName("perso")
        self.tabWidget.addTab(self.perso, "")
        self.jeux = QtWidgets.QWidget()
        self.jeux.setObjectName("jeux")
        self.tabWidget.addTab(self.jeux, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.musique), _translate("MainWindow", "Musique"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.programmation), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AI), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MontageVideo), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.perso), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jeux), _translate("MainWindow", "Page"))
