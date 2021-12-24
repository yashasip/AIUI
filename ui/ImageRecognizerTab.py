from PyQt5 import QtCore, QtGui, QtWidgets

from ui.FileHandle import FileHandle

class ImageRecognizerTab:
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()
        self.setupImageRecognizerUi()

    def setupImageRecognizerUi(self):
        self.tabLayout = QtWidgets.QWidget(self.tab)
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.tabLayout.setGeometry(QtCore.QRect(19, 9, 1199, 651))
        self.imageRecognitionLayout = QtWidgets.QVBoxLayout(self.tabLayout)
        self.imageRecognitionLayout.setContentsMargins(0, 0, 0, 0)

        self.imageRecognitionFrame = QtWidgets.QFrame(self.tabLayout)
        self.imageRecognitionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageRecognitionFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.imageSelectorFrame = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.imageSelectorFrame.setGeometry(QtCore.QRect(-1, -1, 1221, 71))
        self.imageSelectorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageSelectorFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.imagePathInputBox = QtWidgets.QLineEdit(self.imageSelectorFrame)
        self.imagePathInputBox.setGeometry(QtCore.QRect(270, 10, 601, 31))
        self.imagePathInputBox.setObjectName("imagePathInputBox")

        self.imageFileLabel = QtWidgets.QLabel(self.imageSelectorFrame)
        self.imageFileLabel.setGeometry(QtCore.QRect(190, 10, 71, 31))
        self.imageFileLabel.setText("Image File:")
        
        self.chooseImageBtn = QtWidgets.QPushButton(self.imageSelectorFrame)
        self.chooseImageBtn.setGeometry(QtCore.QRect(880, 10, 93, 31))
        self.chooseImageBtn.setText("Choose Image")
        
        self.imageRecognitionLine1 = QtWidgets.QFrame(self.imageSelectorFrame)
        self.imageRecognitionLine1.setGeometry(QtCore.QRect(0, 60, 1221, 20))
        self.imageRecognitionLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine1.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.recognizingTypeFrame = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.recognizingTypeFrame.setGeometry(QtCore.QRect(0, 70, 1221, 41))
        self.recognizingTypeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recognizingTypeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.recogntionTypeLabel = QtWidgets.QLabel(self.recognizingTypeFrame)
        self.recogntionTypeLabel.setGeometry(QtCore.QRect(250, 10, 101, 21))
        self.recogntionTypeLabel.setText("Recognition Type:")

        self.taggingRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.taggingRadioBtn.setGeometry(QtCore.QRect(430, 10, 95, 20))
        self.taggingRadioBtn.setChecked(True)
        self.taggingRadioBtn.setText("Tagging")

        self.categorizeRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.categorizeRadioBtn.setGeometry(QtCore.QRect(580, 10, 111, 20))
        self.categorizeRadioBtn.setText("Catergorize")
        
        self.facialRecognitionRadioBtn = QtWidgets.QRadioButton(self.recognizingTypeFrame)
        self.facialRecognitionRadioBtn.setGeometry(QtCore.QRect(760, 10, 141, 20))
        self.facialRecognitionRadioBtn.setText("Facial Recognition")

        self.imageRecognitionLine2 = QtWidgets.QFrame(self.recognizingTypeFrame)
        self.imageRecognitionLine2.setGeometry(QtCore.QRect(0, 30, 1221, 20))
        self.imageRecognitionLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.imageViewBox = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.imageViewBox.setGeometry(QtCore.QRect(260, 130, 640, 360))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.imageViewBox.setSizePolicy(sizePolicy)
        self.imageViewBox.setAlignment(QtCore.Qt.AlignCenter)
        self.imageViewBox.setText("No Image Choosen")

        self.imageRecognitionLine3 = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.imageRecognitionLine3.setGeometry(QtCore.QRect(0, 490, 1221, 20))
        self.imageRecognitionLine3.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.resultHeadingLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.resultHeadingLabel.setGeometry(QtCore.QRect(570, 500, 51, 21))
        self.resultHeadingLabel.setText("Tagging")

        self.imageRecognitionLine4 = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.imageRecognitionLine4.setGeometry(QtCore.QRect(0, 520, 1221, 16))
        self.imageRecognitionLine4.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine4.setFrameShadow(QtWidgets.QFrame.Sunken)


        self.resultLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.resultLabel.setGeometry(QtCore.QRect(430, 540, 31, 21))
        self.resultLabel.setText("Tag")

        self.accuracyLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.accuracyLabel.setGeometry(QtCore.QRect(430, 570, 55, 16))
        self.accuracyLabel.setText("Accuracy")

        self.extraLabel = QtWidgets.QLabel(self.imageRecognitionFrame)
        self.extraLabel.setGeometry(QtCore.QRect(430, 600, 55, 16))
        self.extraLabel.setText("TextLabel")

        self.pushButton = QtWidgets.QPushButton(self.imageRecognitionFrame)
        self.pushButton.setGeometry(QtCore.QRect(530, 620, 151, 28))
        self.pushButton.setText("Show Additional Tags")
        
        self.imageRecognitionLine5 = QtWidgets.QFrame(self.imageRecognitionFrame)
        self.imageRecognitionLine5.setGeometry(QtCore.QRect(0, 650, 1221, 20))
        self.imageRecognitionLine5.setFrameShape(QtWidgets.QFrame.HLine)
        self.imageRecognitionLine5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.imageRecognitionLayout.addWidget(self.imageRecognitionFrame)
