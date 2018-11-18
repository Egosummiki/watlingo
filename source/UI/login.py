# UI Package
# Login dialog

# Date: 16/11/2018
# Author: Mikołaj Bednarek

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import Path
from loginManager import *

class CreateUserWindow(QDialog):

    def handle(self):
        if not self.textField.text():
            QMessageBox.warning(self, "Puste Pole", "Pole \"Nazwa użytkownika\" nie może być puste.")
        else:
            pass

    def __init__(self, parent):

        QDialog.__init__(self, parent)

        self.setWindowTitle("Dodaj użytkownika")

        self.layout = QVBoxLayout()
        self.layoutButtons = QHBoxLayout()

        self.label = QLabel()
        self.label.setText("Nazwa użytkownika")

        self.textField = QLineEdit()

        self.buttonCancel = QPushButton()
        self.buttonCancel.setText("Anuluj")
        self.buttonCancel.released.connect(self.close)
        self.buttonAdd = QPushButton()
        self.buttonAdd.setText("Dodaj")
        self.buttonAdd.released.connect(self.handle)

        self.layoutButtons.addWidget(self.buttonCancel)
        self.layoutButtons.addWidget(self.buttonAdd)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textField)
        self.layout.addLayout(self.layoutButtons)

        self.setLayout(self.layout)

class LoginWindow(QWidget):

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

        self.setWindowTitle("Wybierz Użytkownika")

        # Init main layout
        self.mainLayout = QHBoxLayout()

        # Add coures view
        self.usersView = QListWidget()
        self.usersView.setStyleSheet("font-size: 20pt")

        self.usersView.addItems(loginManager.users)

        self.mainLayout.addWidget(self.usersView)

        # Create right layout with buttons
        self.rightLayout = QVBoxLayout()

        self.buttonStart = QPushButton()
        self.buttonStart.setText("Wybierz")
        self.rightLayout.addWidget(self.buttonStart)

        self.buttonCreate = QPushButton()
        self.buttonCreate.setText("Stwórz użytkownika")
        self.buttonCreate.released.connect(self.displayAddUserWindow)
        self.rightLayout.addWidget(self.buttonCreate)

        self.buttonQuit = QPushButton()
        self.buttonQuit.setText("Wyjdź")
        self.buttonQuit.released.connect(self.quitApplication)
        self.rightLayout.addWidget(self.buttonQuit)


        # Add layout and set aligment to top
        self.mainLayout.addLayout(self.rightLayout)
        self.mainLayout.setAlignment(self.rightLayout, Qt.AlignTop)

        self.setLayout(self.mainLayout)

    def displayAddUserWindow(self):
        addUser = CreateUserWindow(self)
        addUser.show()

    def quitApplication(self):
        sys.exit(0)
