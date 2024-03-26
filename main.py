
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import MainWindowClass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Initialisation de l'application Qt avec les arguments du système.

    MainWindow = MainWindowClass()
    # Création d'une instance de MainWindowClass.

    MainWindow.show()
    # Affichage de la fenêtre principale.

    sys.exit(app.exec())
    # Exécution de l'application et sortie propre à la fermeture.

