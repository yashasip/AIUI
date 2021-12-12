from PyQt5 import QtCore, QtGui, QtWidgets


class MenuBar:
    def __init__(self, parent) -> None:
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.actionCheck = QtWidgets.QAction(parent)
        self.menuExit = QtWidgets.QMenu(self.menubar)

        parent.setMenuBar(self.menubar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1275, 26))
        self.menuFile.addAction(self.actionCheck)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.menuFile.setTitle("File")
        self.menuExit.setTitle("Exit")
        self.actionCheck.setText("Check")
