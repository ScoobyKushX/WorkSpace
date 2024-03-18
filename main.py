
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow(QMainWindow)
    MainWindow.show()
    sys.exit(app.exec())