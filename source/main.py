#!/usr/bin/python

##### Wat Lingo #####

# Projekt na metodyki wytwarzania oprogramowania.

# Main program file.
# Initialisation of the whole program.

# Date: 29/10/2018
# Author: Mikołaj Bednarek

import sys
import platform
from PyQt5.QtWidgets import *
from UI.login import *
from loginManager import *
from UI.lessons import LessonsWindow
from UI.courses import CoursesWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    loginWindow = LoginWindow(app)
    loginWindow.show()

    sys.exit(app.exec_())
