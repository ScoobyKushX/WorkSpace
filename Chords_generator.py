from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsLineItem, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class PartitionWidget(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.draw_staff()
        self.add_clef()

    def draw_staff(self):
        for i in range(5):  # 5 lignes pour une portée standard
            self.scene.addLine = QGraphicsLineItem(0, i * 10, 200, i * 10)

    def add_clef(self):
        pixmap = QPixmap('clef_de_sol.png')  # Assurez-vous d'avoir une image de clé de sol
        clef = QGraphicsPixmapItem(pixmap)
        clef.setPos(0, 0)  # Positionnez la clé de sol correctement
        self.scene.addItem(clef)