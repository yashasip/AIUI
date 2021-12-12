from PyQt5 import QtCore, QtGui, QtWidgets


class FileHandle:
    def __init__(self, parent) -> None:
        self.binaryFileSelectorFrame = QtWidgets.QFrame(parent)
        self.filePathInputBox = QtWidgets.QLineEdit(self.binaryFileSelectorFrame)
        self.fileLabel = QtWidgets.QLabel(self.binaryFileSelectorFrame)
        self.chooseFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)
        self.fileTypeComboBox = QtWidgets.QComboBox(self.binaryFileSelectorFrame)
        self.viewFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)

        self.setupFileHandle()

    def setupFileHandle(self):
        self.binaryFileSelectorFrame.setGeometry(QtCore.QRect(-1, -1, 1211, 91))

        self.filePathInputBox.setGeometry(QtCore.QRect(210, 20, 761, 31))

        self.fileLabel.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.fileLabel.setText("File:")

        self.chooseFileButton.setGeometry(QtCore.QRect(560, 60, 93, 28))
        self.chooseFileButton.setText("Choose File")

        self.fileTypeComboBox.setGeometry(QtCore.QRect(980, 20, 91, 31))
        self.fileTypeComboBox.setToolTip("Choose File Type")
        self.fileTypeComboBox.setStatusTip("Select File Type")

        self.viewFileButton.setGeometry(QtCore.QRect(660, 60, 93, 28))
        self.viewFileButton.setText("View")
