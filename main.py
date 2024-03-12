
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QScreen
from integrated_application import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    screen_geometry = QScreen.availableGeometry(app.primaryScreen())
    window.setGeometry(screen_geometry)
    window.show()
    sys.exit(app.exec())
