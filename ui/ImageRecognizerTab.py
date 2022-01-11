from PyQt5 import QtCore, QtGui, QtWidgets

from handle.FileHandle import FileHandle
from handle.ImaggaAPIHandler import ImaggaAPIHandler
from requests import exceptions

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
        self.submitButton = QtWidgets.QPushButton(self.imageRecognitionFrame)
        self.viewJsonResults = QtWidgets.QPushButton(self.imageRecognitionFrame)
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

        self.submitButton.setGeometry(QtCore.QRect(530, 620, 151, 28))
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.runRecognizer)

        self.viewJsonResults.setGeometry(QtCore.QRect(1062, 620, 132, 24))
        self.viewJsonResults.setText('View Json Results')
        self.viewJsonResults.setHidden(True)
        self.viewJsonResults.clicked.connect(self.viewJsonResultsWindow)

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
        if not self.imagePathInputBox.text(): # dialog box
            return
            
        self.recognitionType = self.recognitionTypeGroup.checkedButton().text()
        self.setResultHeaderLabel()
        self.submitButton.setDisabled(True)
        self.submitButton.setText('Loading...')
        self.submitButton.repaint()


        self.apiHandler = ImaggaAPIHandler(self.imagePath, self.recognitionType)
        try:
            self.resultData = self.apiHandler.APIHandle()
        except exceptions.ConnectionError:
            self.displayNoResults('Connection Error')
            return
        finally:
            self.submitButton.setEnabled(True)
            self.submitButton.setText('Submit')
        
        print(self.resultData)
        self.displayResults()

    def displayResults(self):
        for item in self.resultLabels:
            item.setText('')
        
        if not self.resultData:
            self.displayNoResults()
            return

        self.viewJsonResults.setVisible(True)

        for index, item  in enumerate(self.resultData[0].items()):
            key, value = item
            self.resultLabels[index].setGeometry(QtCore.QRect(540, 535 + 30 * index, 300, 21))
            self.resultLabels[index].setText(key + ': ' + value.title())

    def displayNoResults(self, failMessageType):
        self.resultLabels[1].setGeometry(QtCore.QRect(540, 565, 300, 21))
        if failMessageType == 'Facial Detection':
            self.resultLabels[1].setText('No human faces detected in this image')
        elif failMessageType == 'Connection Error':
            self.resultLabels[1].setText('No internet connection found')
        else:
            self.resultLabels[1].setText('No Results Found')


    def setResultHeaderLabel(self):
        self.resultHeadingLabel.setText(self.recognitionType)

    def viewJsonResultsWindow(self):
        self.setupJsonResultsWindow(self.apiHandler.getJsonResult())

    def setupJsonResultsWindow(self, results):
        jsonResultsWindow = QtWidgets.QDialog()
        jsonResultsWindow.resize(509, 469)

        self.jsonResultsTextBox = QtWidgets.QPlainTextEdit(jsonResultsWindow)
        self.jsonResultsTextBox.setGeometry(QtCore.QRect(20, 40, 471, 381))
        self.jsonResultsTextBox.setPlainText(results)

        self.okButton = QtWidgets.QPushButton(jsonResultsWindow)
        self.okButton.setGeometry(QtCore.QRect(210, 430, 93, 28))
        self.okButton.clicked.connect(lambda: jsonResultsWindow.done(0))

        self.jsonResultsLabel = QtWidgets.QLabel(jsonResultsWindow)
        self.jsonResultsLabel.setGeometry(QtCore.QRect(20, 10, 91, 21))

        jsonResultsWindow.setWindowTitle("All Results")
        self.okButton.setText("OK")

        self.jsonResultsLabel.setText("Json Results")
        jsonResultsWindow.show()

        
    