from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Tasks.Task import Task

class TaskPicSelect(Task):

    def __init__(self, taskData):
        Task.__init__(self, taskData)

        layout = QHBoxLayout()

        self.radios = []

        for option in taskData["options"]:
            subLayout = QVBoxLayout()
            radio = QRadioButton(option["text"])
            self.radios.append(radio)
            subLayout.addWidget(radio)
            imageLabel = QLabel()
            imageLabel.setFixedSize(200, 200)
            imageLabel.setPixmap(QPixmap("resources/" + option["res"]).scaled(200, 200))
            subLayout.addWidget(imageLabel)
            layout.addLayout(subLayout)

        self.setLayout(layout)

    def checkAnswer(self):
        return self.radios[self.data["answer"]].isChecked()

    def getCorrectAnswer(self):
        return self.data["options"][self.data["answer"]]["text"]
