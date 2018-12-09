from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class LessonsWindow(QWidget):

    def metoda():
        pass

    def __init__(self, lessonManager):

        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.button = QPushButton()
        self.button.setText("Przycisk")

        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

