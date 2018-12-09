# Interface Package
# Courses view widget class

# Date: 29/10/2018
# Author: Mikołaj Bednarek

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CourseManager import CourseManager
from LessonManager import LessonManager
from Interface.Lessons import LessonsWindow

lessonWindow = {}

class CoursesWindow(QWidget):

    def __init__(self, app):

        # Init the super class
        QWidget.__init__(self)

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

        # Init main layout
        self.mainLayout = QHBoxLayout()

        # Add coures view
        self.coursesView = QListWidget()
        self.coursesView.setStyleSheet("font-size: 20pt")
        for course in CourseManager():
            self.coursesView.addItem(course['name'])

        self.mainLayout.addWidget(self.coursesView)

        # Create right layout with buttons
        self.rightLayout = QVBoxLayout()

        self.buttonStart = QPushButton()
        self.buttonStart.setText("Rozpocznij")
        self.buttonStart.released.connect(self.selectCourse)
        self.rightLayout.addWidget(self.buttonStart)

        self.buttonQuit = QPushButton()
        self.buttonQuit.setText("Wyjdź")
        self.buttonQuit.released.connect(self.quitApplication)
        self.rightLayout.addWidget(self.buttonQuit)


        # Add layout and set aligment to top
        self.mainLayout.addLayout(self.rightLayout)
        self.mainLayout.setAlignment(self.rightLayout, Qt.AlignTop)

        self.setLayout(self.mainLayout)

    def selectCourse(self):
        global lessonWindow
        lessonWindow = LessonsWindow(
                CourseManager().getLessonManager(self.coursesView.currentRow()))

        lessonWindow.show()
        self.close()

    def quitApplication(self):
        sys.exit(0)

