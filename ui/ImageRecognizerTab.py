from PyQt5 import QtCore, QtGui, QtWidgets

from handle.FileHandle import FileHandle
from handle.ImaggaAPIHandler import ImaggaAPIHandler

class ImageRecognizerTab:
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()
        self.tabLayout = QtWidgets.QWidget(self.tab)
        self.imageRecognitionFrame = QtWidgets.QFrame(self.tabLayout)
        self.imageSelectorFrame = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.imagePathInputBox = QtWidgets.QLineEdit(self.imageSelectorFrame)
        self.imageFileLabel = QtWidgets.QLabel(self.imageSelectorFrame)
        self.chooseImageBtn = QtWidgets.QPushButton(self.imageSelectorFrame)
        self.imageRecognitionLine1 = QtWidgets.QFrame(self.imageSelectorFrame)
        self.recognizingTypeFrame = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.recogntionTypeLabel = QtWidgets.QLabel(self.recognizingTypeFrame)
        self.taggingRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.categorizeRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.facialRecognitionRadioBtn = QtWidgets.QRadioButton(
            self.recognizingTypeFrame
        )
        self.recognitionTypeGroup = QtWidgets.QButtonGroup(self.imageRecognitionFrame)
        self.imageRecognitionLine2 = QtWidgets.QFrame(self.recognizingTypeFrame)
        self.imageViewBox = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.imageRecognitionLine3 = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.resultHeadingLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.imageRecognitionLine4 = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.resultLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.accuracyLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.extraLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.pushButton = QtWidgets.QPushButton(self.imageRecognitionFrame)
        self.imageRecognitionLine5 = QtWidgets.QFrame(self.imageRecognitionFrame)

        self.imageFilters = "Image File (*.jpg *.jpeg *.png) "

        self.fileHandler = FileHandle(self.imageRecognitionFrame, self.imageFilters)

        self.recognitionType = None
        self.resultLabels = [QtWidgets.QLabel(self.imageRecognitionFrame) for i in range(4)]

        self.setupImageRecognizerUi()

    def setupImageRecognizerUi(self):
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.tabLayout.setGeometry(QtCore.QRect(19, 9, 1199, 651))
        self.imageRecognitionLayout = QtWidgets.QVBoxLayout(self.tabLayout)
        self.imageRecognitionLayout.setContentsMargins(0, 0, 0, 0)

        self.imageRecognitionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageRecognitionFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.imageSelectorFrame.setGeometry(QtCore.QRect(-1, -1, 1221, 71))
        self.imageSelectorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageSelectorFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.imagePathInputBox.setGeometry(QtCore.QRect(270, 10, 601, 31))
        self.imagePathInputBox.setReadOnly(True)
        # self.imagePathInputBox.textChanged.connect(self.runRecognizer)

        self.imageFileLabel.setGeometry(QtCore.QRect(190, 10, 71, 31))
        self.imageFileLabel.setText("Image File:")

        self.chooseImageBtn.setGeometry(QtCore.QRect(880, 10, 93, 31))
        self.chooseImageBtn.clicked.connect(self.getImage)
        self.chooseImageBtn.setText("Choose Image")

        self.imageRecognitionLine1.setGeometry(QtCore.QRect(0, 60, 1221, 20))
        self.imageRecognitionLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine1.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.recognizingTypeFrame.setGeometry(QtCore.QRect(0, 70, 1221, 41))
        self.recognizingTypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recognizingTypeFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.recogntionTypeLabel.setGeometry(QtCore.QRect(250, 10, 101, 21))
        self.recogntionTypeLabel.setText("Recognition Type:")

        self.taggingRadioBtn.setGeometry(QtCore.QRect(430, 10, 95, 20))
        self.taggingRadioBtn.setText("Tagging")
        self.taggingRadioBtn.setChecked(True)

        self.categorizeRadioBtn.setGeometry(QtCore.QRect(580, 10, 111, 20))
        self.categorizeRadioBtn.setText("Categorize")

        self.facialRecognitionRadioBtn.setGeometry(QtCore.QRect(760, 10, 141, 20))
        self.facialRecognitionRadioBtn.setText("Facial Detection")

        self.recognitionTypeGroup.addButton(self.taggingRadioBtn)
        self.recognitionTypeGroup.addButton(self.categorizeRadioBtn)
        self.recognitionTypeGroup.addButton(self.facialRecognitionRadioBtn)

        self.imageRecognitionLine2.setGeometry(QtCore.QRect(0, 30, 1221, 20))
        self.imageRecognitionLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.imageViewBox.setGeometry(QtCore.QRect(260, 130, 640, 360))

        self.imageViewBox.setSizePolicy(self.sizePolicy)
        self.imageViewBox.setAlignment(QtCore.Qt.AlignCenter)
        self.imageViewBox.setText("No Image Chosen")

        self.imageRecognitionLine3.setGeometry(QtCore.QRect(0, 490, 1221, 20))
        self.imageRecognitionLine3.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.resultHeadingLabel.setGeometry(QtCore.QRect(570, 500, 130, 21))
        self.resultHeadingLabel.setText("Tagging")

        self.imageRecognitionLine4.setGeometry(QtCore.QRect(0, 520, 1221, 16))
        self.imageRecognitionLine4.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.pushButton.setGeometry(QtCore.QRect(530, 620, 151, 28))
        self.pushButton.setText("Submit")
        self.pushButton.clicked.connect(self.runRecognizer)

        self.imageRecognitionLine5.setGeometry(QtCore.QRect(0, 650, 1221, 20))
        self.imageRecognitionLine5.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.imageRecognitionLayout.addWidget(self.imageRecognitionFrame)

    
    def getImage(self):
        self.imagePath = self.fileHandler.chooseFile()
        self.imagePathInputBox.setText(self.imagePath)
        image = QtGui.QPixmap(self.imagePath)
        self.imageViewBox.setPixmap(image)
        self.imageViewBox.setScaledContents(True)

    def runRecognizer(self):
        self.recognitionType = self.recognitionTypeGroup.checkedButton().text()
        self.setResultHeaderLabel()

        if self.imagePath == None:
            return

        apiHandler = ImaggaAPIHandler(self.imagePath, self.recognitionType)
        self.resultData = apiHandler.APIHandle()
        print(self.resultData)
        self.displayResults()

    def displayResults(self):
        for item in self.resultLabels:
            item.setText('')

        # if no people present won't work, fd won't work, align the labels, overflow block
        for item, index  in zip(self.resultData[0].items(),range(len(self.resultData[0]))):
            key, value = item
            if index == 3:
                self.resultLabels[index].setGeometry(QtCore.QRect(625, 540 + 30 * (index - 1), 300, 21))
            else:
                self.resultLabels[index].setGeometry(QtCore.QRect(540, 540 + 30 * index, 300, 21))
            self.resultLabels[index].setText(key + ': ' + value)



    def setResultHeaderLabel(self):
        self.resultHeadingLabel.setText(self.recognitionType)

        
    