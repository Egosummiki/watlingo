from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Tasks.Select import TaskSelect
from Tasks.Translate import TaskTranslate
from Tasks.PicSelect import TaskPicSelect

class LessonView(QWidget):

    def __init__(self, lesson):

        QWidget.__init__(self)

        self.lesson = lesson

        self.width = 500
        self.height = 400

        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Lekcja - {}".format(lesson['name']))

        self.mainLayout = QVBoxLayout()

        self.label = QLabel()
        self.mainLayout.addWidget(self.label)

        self.buttonLayout = QHBoxLayout()

        self.taskWidget = None

        self.containerLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.containerLayout)
        
        self.buttonConfirm = QPushButton("Ok")
        self.buttonConfirm.released.connect(self.checkAnswer)
        self.buttonSkip = QPushButton("Pomiń")
        self.buttonPrev = QPushButton("Poprzednie zadanie")

        self.buttonLayout.addWidget(self.buttonPrev)
        self.buttonLayout.addWidget(self.buttonSkip)
        self.buttonLayout.addWidget(self.buttonConfirm)

        self.mainLayout.addLayout(self.buttonLayout)
        self.setLayout(self.mainLayout)

        self.currentTask = 0

        self.loadTask(self.currentTask)

    def loadTask(self, taskId):
        task = self.lesson['tasks'][taskId]
        self.label.setText(task['question'])
        if self.taskWidget != None:
            self.containerLayout.removeWidget(self.taskWidget)
            self.taskWidget.deleteLater()
        
        if task["type"] == "SELECT":
            self.taskWidget = TaskSelect(task)
        elif task["type"] == "TRANSLATE":
            self.taskWidget = TaskTranslate(task)
        elif task["type"] == "PIC-SELECT":
            self.taskWidget = TaskPicSelect(task)

        self.containerLayout.addWidget(self.taskWidget)

    def checkAnswer(self):
        if self.taskWidget == None:
            return

        if self.taskWidget.checkAnswer():
            QMessageBox.information(self, "Odpowiedź", "Prawidłowa odpowiedź")
        else:
            QMessageBox.warning(self, "Odpowiedź", "Nieprawidłowa odpowiedź, Poprawna odpowiedź to \"{}\""
                    .format(self.taskWidget.getCorrectAnswer()))

        self.loadNextTask()


    def loadNextTask(self):
        self.currentTask += 1
        if self.currentTask < len(self.lesson['tasks']):
            self.loadTask(self.currentTask)
        else:
            QMessageBox.information(self, "Lekcja", "Lekcja została ukończona")
            self.close()

