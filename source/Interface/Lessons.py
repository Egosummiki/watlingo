from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class LessonsWindow(QWidget):

    def metoda():
        pass

    def __init__(self, lessonManager):

        QWidget.__init__(self)

        self.lessonManager = lessonManager

        # Get screen size and window size
        screenGeo = app.desktop().screenGeometry()
        self.width = 500
        self.height = 400

        # Set window geometry
        self.setGeometry(
                screenGeo.width()  / 2 - self.width  / 2, 
                screenGeo.height() / 2 - self.height / 2, 
                self.width, self.height)

        self.setFixedSize(self.width, self.height)

        self.setWindowTitle("Wybierz Kurs")



