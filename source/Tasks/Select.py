from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Tasks.Task import Task

class TaskSelect(Task):

    def __init__(self, taskData):
        Task.__init__(self, taskData)

        layout = QVBoxLayout()

        self.radios = []

        for option in taskData["options"]:
            radio = QRadioButton(option["text"])
            self.radios.append(radio)
            layout.addWidget(radio)

        self.setLayout(layout)

    def checkAnswer(self):
        return self.radios[self.data["answer"]].isChecked()

    def getCorrectAnswer(self):
        return self.data["options"][self.data["answer"]]["text"]
