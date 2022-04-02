from PyQt5 import QtCore, QtWidgets
from handle.FileHandle import FileHandle



class BinaryClassifierInput:
    '''Binary Classifier Tab File Input Handling
    Holds all Widgets in a Frame
    parent: parent widget where File Input handlind widgets is created'''
    def __init__(self, parent) -> None:
        self.parentWidget = parent
        self.binaryFileSelectorFrame = QtWidgets.QFrame(self.parentWidget)
        self.filePathInputBox = QtWidgets.QLineEdit(self.binaryFileSelectorFrame)
        self.fileLabel = QtWidgets.QLabel(self.binaryFileSelectorFrame)
        self.chooseFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)
        self.viewFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)

        self.fileFilter = "Data Record File(*.csv *.xlsx *.xlsm *.xlsb *.xls) "
        self.filePath = None

        self.fileHandler = FileHandle(parent, self.fileFilter) # File Handler class

        self.setupFileHandle()

    def setupFileHandle(self):
        # binary selector frame
        self.binaryFileSelectorFrame.setGeometry(QtCore.QRect(-1, -1, 1211, 91))

        # File Input Path Box
        self.filePathInputBox.setGeometry(QtCore.QRect(210, 20, 761, 31))
        self.filePathInputBox.setReadOnly(True)# set read only to restrict user from typing or pasting text in box.

        # File Label
        self.fileLabel.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.fileLabel.setText("File:")

        # Choose File BUtton
        self.chooseFileButton.setGeometry(QtCore.QRect(560, 60, 93, 28))
        self.chooseFileButton.setText("Choose File")
        self.chooseFileButton.clicked.connect(self.getFilePath)

        # View File Button
        self.viewFileButton.setGeometry(QtCore.QRect(660, 60, 93, 28))
        self.viewFileButton.setText("View")
        self.viewFileButton.clicked.connect(self.fileHandler.viewFile)
        self.viewFileButton.setEnabled(False)


    # Disabling view button until file is chosen
    def getFilePath(self):
        self.filePath = self.fileHandler.chooseFile()
        if not self.filePath:
            self.viewFileButton.setEnabled(False)
        else:
            self.viewFileButton.setEnabled(True)
        self.filePathInputBox.setText(self.filePath)





