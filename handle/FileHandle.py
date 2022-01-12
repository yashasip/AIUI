from PyQt5 import QtCore, QtGui, QtWidgets
import os


class FileHandle:
    def __init__(self, parent, fileFilter) -> None:
        self.fileFilter = fileFilter
        self.parentWidget = parent
        self.filePath = None

    def chooseFile(self):
        fileObj = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.parentWidget, caption="Choose File", filter=self.fileFilter
        )
        if fileObj[0]:  # if no file is chosen / Cancel button is clicked
            self.filePath = fileObj[0]

        return self.filePath

    def viewFile(self):
        os.startfile(self.filePath)

    def saveFile(self, fileType):
        name = QtWidgets.QFileDialog.getSaveFileName(
            parent=self.parentWidget,
            caption="Save File",
            filter=fileType,
            initialFilter=fileType,
        )
        return name

    def openDirectory(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(
            self.parentWidget,
            caption  = "Open Directory containing the Model",
            options = QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks
        )
        return dir
