from PySide2 import QtCore, QtWidgets, QtGui

class CoursesWindow(QtWidgets.QWidget):

    def __init__(self, app):

        # Init the super class
        QtWidgets.QWidget.__init__(self)

        # Get screen size and set window size
        screenGeo = app.desktop().screenGeometry()
        self.width = 500
        self.height = 400

        # Set window geometry
        self.setGeometry(screenGeo.width() / 2 - self.width / 2, screenGeo.height() / 2 - self.height / 2, self.width, self.height)
        self.setFixedSize(self.width, self.height)


