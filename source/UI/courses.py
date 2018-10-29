# UI Package
# Courses view widget class

# Data: 29/10/2018
# Author: Mikołaj Bednarek

import sys
from PySide2 import QtCore, QtWidgets, QtGui

class CoursesWindow(QtWidgets.QWidget):

    def __init__(self, app):

        # Init the super class
        QtWidgets.QWidget.__init__(self)

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

        # Init main layout
        self.mainLayout = QtWidgets.QHBoxLayout()

        # Add coures view
        self.coursesView = QtWidgets.QListWidget()
        self.coursesView.setStyleSheet("font-size: 20pt")
        self.coursesView.addItem("British English")
        self.coursesView.addItem("Español")
        self.coursesView.addItem("Português de Portugal")
        self.coursesView.addItem("Português do Brasil")
        self.mainLayout.addWidget(self.coursesView)

        # Create right layout with buttons
        self.rightLayout = QtWidgets.QVBoxLayout()

        self.buttonStart = QtWidgets.QPushButton()
        self.buttonStart.setText("Rozpocznij")
        self.rightLayout.addWidget(self.buttonStart)

        self.buttonQuit = QtWidgets.QPushButton()
        self.buttonQuit.setText("Wyjdź")
        self.buttonQuit.released.connect(self.quitApplication)
        self.rightLayout.addWidget(self.buttonQuit)


        # Add layout and set aligment to top
        self.mainLayout.addLayout(self.rightLayout)
        self.mainLayout.setAlignment(self.rightLayout, QtCore.Qt.AlignTop)

        self.setLayout(self.mainLayout)

    def quitApplication(self):
        sys.exit(0)

