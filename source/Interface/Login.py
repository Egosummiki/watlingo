# Interface Package
# Login dialog

# Date: 16/11/2018
# Author: Mikołaj Bednarek

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import Path
from UserManager import UserManager
from Interface.Courses import CoursesWindow

coursesWindow = {}

# Dialog which asks the user to input the password
class DialogEnterPassword(QDialog):

    def __init__(self, parent, userid):

        QDialog.__init__(self, parent)

        # Dialog has a label a text field
        # a button to cancel and a button to confirm the input

        self.loginWindow = parent
        self.setWindowTitle("Podaj hasło")
        self.userid = userid

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.field = QLineEdit()
        self.field.setEchoMode(QLineEdit.Password) # Hide the letters

        self.label.setText("Hasło użytkownika {}".format(UserManager().users[userid]['name']))

        self.layoutButtons = QHBoxLayout()
        self.buttonCancel = QPushButton()
        self.buttonCancel.setText("Anuluj")
        self.buttonCancel.setDefault(False)
        self.buttonCancel.released.connect(self.close)
        self.buttonAdd = QPushButton()
        self.buttonAdd.setText("Potwierdź")
        self.buttonAdd.setDefault(True)
        self.buttonAdd.released.connect(self.attempt)

        self.layoutButtons.addWidget(self.buttonCancel)
        self.layoutButtons.addWidget(self.buttonAdd)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.field)
        self.layout.addLayout(self.layoutButtons)

        self.setLayout(self.layout)

    def attempt(self):
        if UserManager().verifyPassword(self.userid, self.field.text()):
            global coursesWindow
            coursesWindow = CoursesWindow(self.loginWindow.application)
            self.close()
            self.loginWindow.close()
            coursesWindow.show()
        else:
            QMessageBox.warning(self, "Hasło", "Wprowadzone złe hasło")

# Dialog that allows user creation
class DialogCreateUser(QDialog):

    def handle(self):
        if self.field.text() and self.fieldPass.text():
            # Field are not empty call the user manager and reload the view
            UserManager().addUser(self.field.text(), self.fieldPass.text())
            self.loginWindow.reloadUsers()
            self.close()
        else:
            # Prompt the user that the one of the fields is empty
            QMessageBox.warning(self, "Puste Pole", "Pola nie mogą być puste.")

    def __init__(self, parent):

        QDialog.__init__(self, parent)

        # The dialog has 2 text fields 
        # one for the username other for the password
        # along which corresponding labels.
        # The dialog also has 2 buttons
        # For cancelation and confirmation

        self.loginWindow = parent
        self.setWindowTitle("Dodaj użytkownika")
        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.label.setText("Nazwa użytkownika")
        self.labelPass = QLabel()
        self.labelPass.setText("Hasło")

        self.field = QLineEdit()
        self.fieldPass = QLineEdit()
        self.fieldPass.setEchoMode(QLineEdit.Password)

        self.layoutButtons = QHBoxLayout()
        self.buttonCancel = QPushButton()
        self.buttonCancel.setText("Anuluj")
        self.buttonCancel.setDefault(False)
        self.buttonCancel.released.connect(self.close)
        self.buttonAdd = QPushButton()
        self.buttonAdd.setText("Dodaj")
        self.buttonAdd.setDefault(True)
        self.buttonAdd.released.connect(self.handle)

        self.layoutButtons.addWidget(self.buttonCancel)
        self.layoutButtons.addWidget(self.buttonAdd)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.field)
        self.layout.addWidget(self.labelPass)
        self.layout.addWidget(self.fieldPass)
        self.layout.addLayout(self.layoutButtons)

        self.setLayout(self.layout)

# The main login window class
class LoginWindow(QWidget):

    # Reload the view
    def reloadUsers(self):
        # Remove everything from the list
        while self.usersView.count() > 0:
            self.usersView.takeItem(0)

        # For each user add their name to the view
        for user in UserManager():
            self.usersView.addItem(user['name'])

    def __init__(self, app):

        # Init the super class
        QWidget.__init__(self)

        self.application = app

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

        self.reloadUsers()

        self.mainLayout.addWidget(self.usersView)

        # Create right layout with buttons
        self.rightLayout = QVBoxLayout()

        self.buttonStart = QPushButton()
        self.buttonStart.setText("Wybierz")
        self.buttonStart.released.connect(self.selectUser)
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
        addUser = DialogCreateUser(self)
        addUser.show()

    def selectUser(self):
        enterPass = DialogEnterPassword(self, self.usersView.currentRow())
        enterPass.show()

    def quitApplication(self):
        sys.exit(0)
