from PyQt5 import QtWidgets
import os


class FileHandle:
    '''Controls all File Opening, Saving Directory'''
    def __init__(self, parent, fileFilter) -> None:
        self.fileFilter = fileFilter # type of file that is to be chosen restriction
        self.parentWidget = parent
        self.filePath = None

    def chooseFile(self): # opens file dialog which is used to select the file name and return its path as a string
        fileObj = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.parentWidget, caption="Choose File", filter=self.fileFilter
        )
        if fileObj[0]:  # if no file is chosen / Cancel button is clicked
            self.filePath = fileObj[0]

        return self.filePath

    def viewFile(self): # opens file using a desktop app
        os.startfile(self.filePath)

    def saveFile(self, fileType): # returns directory path along with the filename where a file is to be saved
        name = QtWidgets.QFileDialog.getSaveFileName(
            parent=self.parentWidget,
            caption="Save File",
            filter=fileType,
            initialFilter=fileType,
        )
        return name

    def openDirectory(self): # returns directory path that is to be opened
        dir = QtWidgets.QFileDialog.getExistingDirectory(
            self.parentWidget,
            caption  = "Open Directory containing the Model",
            options = QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks
        )
        return dir
