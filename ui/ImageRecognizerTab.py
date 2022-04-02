from xml.dom.minidom import Element
from PyQt5 import QtCore, QtGui, QtWidgets

from handle.FileHandle import FileHandle
from handle.ImaggaAPIHandler import ImaggaAPIHandler
from requests import exceptions

class ImageRecognizerTab:
    '''Image Recognizer Tab UI components and functionalities'''
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget() # setup tab
        self.tabLayout = QtWidgets.QWidget(self.tab) # setup tab layout
        self.imageRecognitionFrame = QtWidgets.QFrame(self.tabLayout) # image recognition frame, whole tab frame
        self.imageSelectorFrame = QtWidgets.QFrame(self.imageRecognitionFrame) # input frame
        # imageSelector frame ui Elements
        self.imagePathInputBox = QtWidgets.QLineEdit(self.imageSelectorFrame)
        self.imageFileLabel = QtWidgets.QLabel(self.imageSelectorFrame)
        self.chooseImageBtn = QtWidgets.QPushButton(self.imageSelectorFrame)
        self.imageRecognitionLine1 = QtWidgets.QFrame(self.imageSelectorFrame)
        # recognition type select frame and related widgets
        self.recognizingTypeFrame = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.recogntionTypeLabel = QtWidgets.QLabel(self.recognizingTypeFrame)
        self.taggingRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.categorizeRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.facialRecognitionRadioBtn = QtWidgets.QRadioButton(
            self.recognizingTypeFrame
        )
        self.recognitionTypeGroup = QtWidgets.QButtonGroup(self.imageRecognitionFrame) # recognition type group
        # view image components
        self.imageRecognitionLine2 = QtWidgets.QFrame(self.recognizingTypeFrame)
        self.imageViewBox = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.imageRecognitionLine3 = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.resultHeadingLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.sizePolicy = QtWidgets.QSizePolicy( # size policy for image
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        self.imageRecognitionLine4 = QtWidgets.QFrame(self.imageRecognitionFrame)
        # results section
        self.resultLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.accuracyLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.extraLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.submitButton = QtWidgets.QPushButton(self.imageRecognitionFrame)
        self.viewJsonResults = QtWidgets.QPushButton(self.imageRecognitionFrame) # view json results
        self.imageRecognitionLine5 = QtWidgets.QFrame(self.imageRecognitionFrame)

        self.imageFilters = "Image File (*.jpg *.jpeg *.png)" # restricting image extensions

        self.fileHandler = FileHandle(self.imageRecognitionFrame, self.imageFilters) # File Handler object for image

        self.recognitionType = None # initial recognition type value
        self.resultLabels = [QtWidgets.QLabel(self.imageRecognitionFrame) for i in range(4)] # sets up result labels

        self.setupImageRecognizerUi() # sets up all widgets of the image recognizers

    def setupImageRecognizerUi(self): # set up all widgets of image recognizers
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
        self.imagePathInputBox.setReadOnly(True) # restrict user from typing and pasting input file path 

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
        self.taggingRadioBtn.setChecked(True) # set tagging as checked initially

        self.categorizeRadioBtn.setGeometry(QtCore.QRect(580, 10, 111, 20))
        self.categorizeRadioBtn.setText("Categorize")

        self.facialRecognitionRadioBtn.setGeometry(QtCore.QRect(760, 10, 141, 20))
        self.facialRecognitionRadioBtn.setText("Facial Detection")

        self.recognitionTypeGroup.addButton(self.taggingRadioBtn) # add all check boxes to recognition group
        self.recognitionTypeGroup.addButton(self.categorizeRadioBtn)
        self.recognitionTypeGroup.addButton(self.facialRecognitionRadioBtn)

        self.imageRecognitionLine2.setGeometry(QtCore.QRect(0, 30, 1221, 20))
        self.imageRecognitionLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.imageViewBox.setGeometry(QtCore.QRect(260, 130, 640, 360))

        self.imageViewBox.setSizePolicy(self.sizePolicy) # sets up size policy to make sure image does not overflow
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
        self.viewJsonResults.setHidden(True) # hide initially
        self.viewJsonResults.clicked.connect(self.viewJsonResultsWindow)

        self.imageRecognitionLine5.setGeometry(QtCore.QRect(0, 650, 1221, 20))
        self.imageRecognitionLine5.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.imageRecognitionLayout.addWidget(self.imageRecognitionFrame) # add frame to tab

    
    def getImage(self): # gets image path using file dialog and display image in ui 
        self.imagePath = self.fileHandler.chooseFile()
        self.imagePathInputBox.setText(self.imagePath)
        image = QtGui.QPixmap(self.imagePath) # create an pixmap objet
        self.imageViewBox.setPixmap(image) # display image
        self.imageViewBox.setScaledContents(True) # to prevent overflow

    def runRecognizer(self): # runs recognition based on type of recognition
        if not self.imagePathInputBox.text(): # dialog box
            return
            
        self.recognitionType = self.recognitionTypeGroup.checkedButton().text() # get selected radio button
        self.setResultHeaderLabel() # sets up result header label
        self.submitButton.setDisabled(True) # disable when calling api
        self.submitButton.setText('Loading...') # loading message
        self.submitButton.repaint() # repaint to show button changes


        self.apiHandler = ImaggaAPIHandler(self.imagePath, self.recognitionType) # ImaggaAPIHandle object to run all image apis
        try:
            self.resultData = self.apiHandler.APIHandle()
        except exceptions.ConnectionError: # no internet connection
            self.displayNoResults('Connection Error')
            return
        finally: # enable submit again
            self.submitButton.setEnabled(True)
            self.submitButton.setText('Submit')
        
        self.displayResults()

    def displayResults(self): # setup all result labels
        for item in self.resultLabels:  # reset all label values
            item.setText('')
        
        if not self.resultData:
            self.displayNoResults() # when no result found
            return

        self.viewJsonResults.setVisible(True) # set viewJsonRessults button visible

        for index, item  in enumerate(self.resultData[0].items()): # sets text values of result labels
            key, value = item
            self.resultLabels[index].setGeometry(QtCore.QRect(540, 535 + 30 * index, 300, 21))
            self.resultLabels[index].setText(key + ': ' + value.title())

    def displayNoResults(self, failMessageType=None): # displays appropriate message on failure
        self.resultLabels[1].setGeometry(QtCore.QRect(540, 565, 300, 21))
        if self.recognitionType == 'Facial Detection':
            self.resultLabels[1].setText('No human faces detected in this image')
        elif failMessageType == 'Connection Error':
            self.resultLabels[1].setText('No internet connection found')
        else:
            self.resultLabels[1].setText('No Results Found')


    def setResultHeaderLabel(self):
        self.resultHeadingLabel.setText(self.recognitionType)

    def viewJsonResultsWindow(self): # calls the setupJsonResultsWIndow()
        self.setupJsonResultsWindow(self.apiHandler.getJsonResult())

    def setupJsonResultsWindow(self, results): # view results json dialog window
        jsonResultsWindow = QtWidgets.QDialog()
        jsonResultsWindow.resize(509, 469)

        self.jsonResultsTextBox = QtWidgets.QPlainTextEdit(jsonResultsWindow)
        self.jsonResultsTextBox.setGeometry(QtCore.QRect(20, 40, 471, 381))
        self.jsonResultsTextBox.setPlainText(results) # sets all the result values

        self.okButton = QtWidgets.QPushButton(jsonResultsWindow)
        self.okButton.setGeometry(QtCore.QRect(210, 430, 93, 28))
        self.okButton.clicked.connect(lambda: jsonResultsWindow.done(0)) # on completion kill dialog box

        self.jsonResultsLabel = QtWidgets.QLabel(jsonResultsWindow)
        self.jsonResultsLabel.setGeometry(QtCore.QRect(20, 10, 91, 21))

        jsonResultsWindow.setWindowTitle("All Results")# setiing texts of dialog widget components
        self.okButton.setText("OK")

        self.jsonResultsLabel.setText("Json Results")
        jsonResultsWindow.show()

        
    