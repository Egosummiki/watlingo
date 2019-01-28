from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Interface.LessonView import *

lessonView = None

class LessonsWindow(QWidget):

    def metoda():
        pass

    def __init__(self, lessonManager):

        QWidget.__init__(self)

        self.lessonManager = lessonManager

        self.width = 500
        self.height = 400

        self.setFixedSize(self.width, self.height)
        self.setWindowTitle("Wybierz Lekcje")

        self.mainLayout = QHBoxLayout()
        self.lessonView = QListWidget()
        self.lessonView.setStyleSheet("font-size: 20pt")

        for lesson in self.lessonManager:
            self.lessonView.addItem(lesson["name"])

        self.buttonLayout = QVBoxLayout()
        self.buttonLoad = QPushButton("Rozpocznij")
        self.buttonLoad.released.connect(self.loadCourse)
        self.buttonLayout.addWidget(self.buttonLoad)

        self.mainLayout.addWidget(self.lessonView)
        self.mainLayout.addLayout(self.buttonLayout)
        self.setLayout(self.mainLayout)

    def loadCourse(self):
        global lessonView
        lessonView = LessonView(self.lessonManager[self.lessonView.currentRow()])
        lessonView.show()

