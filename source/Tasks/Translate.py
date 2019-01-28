from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Tasks.Task import Task

class TaskTranslate(Task):

    def __init__(self, taskData):
        Task.__init__(self, taskData)

        layout = QVBoxLayout()

        self.edit = QLineEdit()
        layout.addWidget(self.edit)
        self.setLayout(layout)

    def checkAnswer(self):
        
        for option in self.data["answers"]:
            if option.lower() == self.edit.text():
                return True

        return False

    def getCorrectAnswer(self):
        return self.data["answers"][0]
