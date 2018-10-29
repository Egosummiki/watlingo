#!/usr/bin/python

##### Wat Lingo #####

# Projekt na metodyki wytwarzania oprogramowania.

# Main program file.
# Initialisation of the whole program.

# Date: 29/10/2018
# Author: Mikołaj Bednarek

import sys
from PySide2 import QtCore, QtWidgets
from UI.courses import CoursesWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    coursesWindow = CoursesWindow(app)
    coursesWindow.show()

    sys.exit(app.exec_())
