
import PySide6
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from ui_form import Ui_Form
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Initialize and display each UI component
        # Example for a button
        self.show()
        self.ui.pushButton.clicked.connect(self.on_button_click)
        self.ui.tabWidget = QTabWidget
        self.ui.widget_playlist = QWidget
        self.ui.verticalLayoutWidget = QWidget
        self.ui.verticalLayout = QVBoxLayout
        self.ui.tab_AI = self.ui.tabWidget.addTab(self.ui.tabWidget ,"Intelligence Artificielle")

        # Example for a text edit
        self.ui.textEdit.textChanged.connect(self.on_text_edit_change)

        # Example for a slider
        self.ui.horizontalSlider.valueChanged.connect(self.on_slider_value_change)

        self.ui.show()

    # Event handler for button click
    def on_button_click(self):
        print("Button clicked!")

    # Event handler for text edit change
    def on_text_edit_change(self):
        print("Text changed!")

    # Event handler for slider value change
    def on_slider_value_change(self, value):
        print(f"Slider value changed: {value}")