# UI Package
# Login dialog

# Date: 16/11/2018
# Author: Mikołaj Bednarek

import sys
import os
from PySide2 import QtCore, QtWidgets, QtGui
from pathlib import Path

class LoginWindow(QtWidgets.QWidget):

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

        self.setWindowTitle("Wybierz Użytkownika")

        # Init main layout
        self.mainLayout = QtWidgets.QHBoxLayout()

        # Add coures view
        self.usersView = QtWidgets.QListWidget()
        self.usersView.setStyleSheet("font-size: 20pt")

        dirs = os.listdir(str(Path.home()) + "/.watlingo")

        for dirName in dirs:
            self.usersView.addItem(dirName)

        self.mainLayout.addWidget(self.usersView)

        # Create right layout with buttons
        self.rightLayout = QtWidgets.QVBoxLayout()

        self.buttonStart = QtWidgets.QPushButton()
        self.buttonStart.setText("Wybierz")
        self.rightLayout.addWidget(self.buttonStart)

        self.buttonCreate = QtWidgets.QPushButton()
        self.buttonCreate.setText("Stwórz użytkownika")
        self.rightLayout.addWidget(self.buttonCreate)

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
