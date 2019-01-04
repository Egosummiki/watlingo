from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class LessonsWindow(QWidget):

    def metoda():
        pass

    def __init__(self, lessonManager):

        QWidget.__init__(self)

        self.lessonManager = lessonManager

        self.width = 500
        self.height = 400

        self.setFixedSize(self.width, self.height)

        self.setWindowTitle("Wybierz Kurs")



