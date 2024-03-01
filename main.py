from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QScreen
from main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    screen_geometry = QScreen.availableGeometry(app.primaryScreen())
    mainwindow.setGeometry(screen_geometry)
    mainwindow.show()
    sys.exit(app.exec())
