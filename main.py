
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow, MainWindowClass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindowClass(QMainWindow)
    MainWindow.show()
    sys.exit(app.exec())
