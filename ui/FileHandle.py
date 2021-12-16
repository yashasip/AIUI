from PyQt5 import QtCore, QtGui, QtWidgets


class FileHandle:
    def __init__(self, parent) -> None:
        self.parentWidget = parent
        self.binaryFileSelectorFrame = QtWidgets.QFrame(self.parentWidget)
        self.filePathInputBox = QtWidgets.QLineEdit(self.binaryFileSelectorFrame)
        self.fileLabel = QtWidgets.QLabel(self.binaryFileSelectorFrame)
        self.chooseFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)
        self.fileTypeComboBox = QtWidgets.QComboBox(self.binaryFileSelectorFrame)
        self.viewFileButton = QtWidgets.QPushButton(self.binaryFileSelectorFrame)
        self.options=['-','.csv','.xlsx','.xlsm','.xlsb','.xls']

        self.filePath = None

        self.setupFileHandle()


    def setupFileHandle(self):
        self.binaryFileSelectorFrame.setGeometry(QtCore.QRect(-1, -1, 1211, 91))

        self.filePathInputBox.setGeometry(QtCore.QRect(210, 20, 761, 31))

        self.fileLabel.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.fileLabel.setText("File:")

        self.chooseFileButton.setGeometry(QtCore.QRect(560, 60, 93, 28))
        self.chooseFileButton.setText("Choose File")
        self.chooseFileButton.clicked.connect(self.openFile)

        self.fileTypeComboBox.setGeometry(QtCore.QRect(980, 20, 91, 31))
        self.fileTypeComboBox.setToolTip("Choose File Type")
        self.fileTypeComboBox.setStatusTip("Select File Type")
        self.fileTypeComboBox.addItems(self.options)


        self.viewFileButton.setGeometry(QtCore.QRect(660, 60, 93, 28))
        self.viewFileButton.setText("View")
        

    def openFile(self, fileFilter=None):
        import os
        fileObj = QtWidgets.QFileDialog.getOpenFileName(
            parent=self.parentWidget,
            caption = 'Choose File',
            directory= os.getcwd(),
            filter = 'CSV File( *.csv )'
        )
        self.filePath = fileObj[0]
