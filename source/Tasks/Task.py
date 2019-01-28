from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Task(QWidget):

    def __init__(self, taskData):

        QWidget.__init__(self)
        self.data = taskData

    def checkAnswer(self):
        return False

    def getCorrectAnswer(self):
        return ""
