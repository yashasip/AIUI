from PyQt5 import QtCore, QtWidgets
from handle.FileHandle import FileHandle



class BinaryClassifierInput:
    def __init__(self, parent) -> None:
        self.parentWidget = parent
        self.binaryFileSelectorFrame = QtWidgets.QFrame(self.parentWidget)
        self.filePathInputBox = QtWidgets.QLineEdit(self.binaryFileSelectorFrame)
        self.fileLabel = QtWidgets.QLabel(self.binaryFileSelectorFrame)
        self.chooseFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)
        self.viewFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)

        self.fileFilter = "Data Record File(*.csv *.xlsx *.xlsm *.xlsb *.xls) "
        self.filePath = None

        self.fileHandler = FileHandle(parent, self.fileFilter)

        self.setupFileHandle()

    def setupFileHandle(self):
        self.binaryFileSelectorFrame.setGeometry(QtCore.QRect(-1, -1, 1211, 91))

        self.filePathInputBox.setGeometry(QtCore.QRect(210, 20, 761, 31))
        self.filePathInputBox.setReadOnly(True)

        self.fileLabel.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.fileLabel.setText("File:")

        self.chooseFileButton.setGeometry(QtCore.QRect(560, 60, 93, 28))
        self.chooseFileButton.setText("Choose File")

        self.viewFileButton.setGeometry(QtCore.QRect(660, 60, 93, 28))
        self.viewFileButton.setText("View")
        self.viewFileButton.clicked.connect(self.fileHandler.viewFile)
        self.viewFileButton.setEnabled(False)


#Disabling view button until file is chosen
    def getFilePath(self):
        self.filePath = self.fileHandler.chooseFile()
        if not self.filePath:
            self.viewFileButton.setEnabled(False)
        else:
            self.viewFileButton.setEnabled(True)
        self.filePathInputBox.setText(self.filePath)





