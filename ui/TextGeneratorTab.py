from PyQt5 import QtCore, QtWidgets

from handle.FileHandle import FileHandle

class TextGeneratorTab():
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()

        self.textGeneratorFrame = QtWidgets.QFrame(self.tab)
        self.textGeneratorSelectorFrame = QtWidgets.QFrame(self.textGeneratorFrame)

        self.fileLabel = QtWidgets.QLabel(self.textGeneratorSelectorFrame)
        self.fileInputPathBox = QtWidgets.QLineEdit(self.textGeneratorSelectorFrame)
        self.chooseFileButton = QtWidgets.QPushButton(self.textGeneratorSelectorFrame)
        self.viewButton = QtWidgets.QPushButton(self.textGeneratorSelectorFrame)

        self.configGroupBox = QtWidgets.QGroupBox(self.textGeneratorFrame)

        self.excludePagesLabel = QtWidgets.QLabel(self.configGroupBox)
        self.fromLabel = QtWidgets.QLabel(self.configGroupBox)
        self.fromPageSpinBox = QtWidgets.QSpinBox(self.configGroupBox)
        self.toLabel = QtWidgets.QLabel(self.configGroupBox)
        self.toSpinBox = QtWidgets.QSpinBox(self.configGroupBox)

        self.epochsSpinBox = QtWidgets.QSpinBox(self.configGroupBox)
        self.epochsLabel = QtWidgets.QLabel(self.configGroupBox)
        
        self.temperatureLabel = QtWidgets.QLabel(self.configGroupBox)
        self.temperatureSpinBox = QtWidgets.QDoubleSpinBox(self.configGroupBox)

        self.optimizerLabel = QtWidgets.QLabel(self.configGroupBox)
        self.optimizerComboBox = QtWidgets.QComboBox(self.configGroupBox)
        
        self.trainButton = QtWidgets.QPushButton(self.configGroupBox)
        self.saveModelButton = QtWidgets.QPushButton(self.configGroupBox)
        
        self.modelNameLabel = QtWidgets.QLabel(self.configGroupBox)
        self.sequenceLengthLabel = QtWidgets.QLabel(self.configGroupBox)
        self.sequenceLengthSpinBox = QtWidgets.QSpinBox(self.configGroupBox)
        self.batchSizeSpinBox = QtWidgets.QSpinBox(self.configGroupBox)

        self.typeSpaceBoxFrame = QtWidgets.QFrame(self.textGeneratorFrame)
        self.typeSpaceLabel = QtWidgets.QLabel(self.typeSpaceBoxFrame)
        self.typeSpaceBox = QtWidgets.QPlainTextEdit(self.typeSpaceBoxFrame)
        
        self.generateButton = QtWidgets.QPushButton(self.typeSpaceBoxFrame)
        self.saveButton = QtWidgets.QPushButton(self.typeSpaceBoxFrame)
        
        self.textGeneratorLine1 = QtWidgets.QFrame(self.textGeneratorFrame)
        self.textGeneratorLine2 = QtWidgets.QFrame(self.configGroupBox)
        self.textGeneratorLine3 = QtWidgets.QFrame(self.textGeneratorFrame)
        self.textGeneratorLine4 = QtWidgets.QFrame(self.textGeneratorFrame)

        self.fileFilter = 'PDF, Document File(*.pdf *.docx *.doc)'    
        self.fileHandler = FileHandle(self.textGeneratorFrame, self.fileFilter)
        
        self.setupTextGeneratorTab()

        
    def setupTextGeneratorTab(self):
        self.textGeneratorFrame.setGeometry(QtCore.QRect(10, 0, 1219, 691))
        self.textGeneratorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textGeneratorFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.textGeneratorSelectorFrame.setGeometry(QtCore.QRect(0, 0, 1221, 101))
        self.textGeneratorSelectorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textGeneratorSelectorFrame.setFrameShadow(QtWidgets.QFrame.Raised)


        self.fileInputPathBox.setGeometry(QtCore.QRect(270, 20, 681, 31))
        self.fileLabel.setGeometry(QtCore.QRect(230, 20, 31, 31))
        self.fileLabel.setText("File:")

        self.chooseFileButton.setGeometry(QtCore.QRect(510, 60, 93, 31))
        self.chooseFileButton.setText("Choose File")
        self.chooseFileButton.clicked.connect(self.getFilePath)

        self.viewButton.setEnabled(False)
        self.viewButton.setGeometry(QtCore.QRect(620, 60, 93, 31))
        self.viewButton.setText("View")
        self.viewButton.clicked.connect(self.fileHandler.viewFile)

        self.textGeneratorLine1.setGeometry(QtCore.QRect(0, 90, 1221, 20))
        self.textGeneratorLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.textGeneratorLine1.setFrameShadow(QtWidgets.QFrame.Sunken)


        self.configGroupBox.setGeometry(QtCore.QRect(10, 100, 541, 570))
        self.configGroupBox.setTitle("Config")

        self.fromPageSpinBox.setGeometry(QtCore.QRect(160, 50, 81, 31))

        self.excludePagesLabel.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.excludePagesLabel.setText("Exclude Pages")

        self.fromLabel.setGeometry(QtCore.QRect(170, 20, 41, 31))
        self.fromLabel.setText("From")

        self.toLabel.setGeometry(QtCore.QRect(330, 20, 21, 31))
        self.toLabel.setText("To")

        self.batchSizeLabel = QtWidgets.QLabel(self.configGroupBox)
        self.epochsSpinBox.setGeometry(QtCore.QRect(160, 120, 81, 31))

        self.epochsLabel.setGeometry(QtCore.QRect(30, 120, 71, 31))
        self.epochsLabel.setText("Epochs")

        self.toSpinBox.setGeometry(QtCore.QRect(300, 50, 81, 31))

        self.optimizerLabel.setGeometry(QtCore.QRect(30, 190, 61, 31))
        self.optimizerLabel.setText("Optimizer")

        self.optimizerComboBox.setGeometry(QtCore.QRect(160, 190, 181, 31))

        self.temperatureLabel.setGeometry(QtCore.QRect(30, 260, 91, 31))

        self.temperatureSpinBox.setGeometry(QtCore.QRect(160, 260, 61, 31))
        self.temperatureSpinBox.setMaximum(1.0)
        self.temperatureSpinBox.setProperty("value", 0.5)
        self.temperatureLabel.setText("Temperature")

        self.sequenceLengthLabel.setGeometry(QtCore.QRect(30, 330, 111, 31))
        self.sequenceLengthLabel.setText("Sequence Length")

        self.batchSizeLabel.setGeometry(QtCore.QRect(30, 400, 71, 31))
        self.batchSizeLabel.setText("Batch Size")

        self.trainButton.setGeometry(QtCore.QRect(220, 470, 111, 31))
        self.trainButton.setText("Train")

        self.saveModelButton.setEnabled(False)
        self.saveModelButton.setGeometry(QtCore.QRect(410, 530, 111, 31))
        self.saveModelButton.setText("Save Model")

        self.textGeneratorLine2.setGeometry(QtCore.QRect(0, 510, 551, 16))
        self.textGeneratorLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.textGeneratorLine2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.modelNameLabel.setGeometry(QtCore.QRect(10, 530, 321, 31))
        self.modelNameLabel.setText("Model Name:")

        self.sequenceLengthSpinBox.setGeometry(QtCore.QRect(160, 330, 111, 31))
        self.sequenceLengthSpinBox.setProperty("value", 99)

        self.batchSizeSpinBox.setGeometry(QtCore.QRect(160, 400, 111, 31))
        self.batchSizeSpinBox.setProperty("value", 64)


        self.typeSpaceBoxFrame.setGeometry(QtCore.QRect(570, 100, 651, 570))
        self.typeSpaceBoxFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.typeSpaceBoxFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.typeSpaceBox.setGeometry(QtCore.QRect(10, 30, 631, 490))
        self.typeSpaceBox.setPlaceholderText("Start Typing Here")

        self.generateButton.setGeometry(QtCore.QRect(230, 528, 93, 31))
        self.generateButton.setText("Generate")

        self.typeSpaceLabel.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.typeSpaceLabel.setText("Type Space")

        self.saveButton.setGeometry(QtCore.QRect(330, 528, 93, 31))
        self.saveButton.setText("Save")

        self.textGeneratorLine3.setGeometry(QtCore.QRect(550, 100, 20, 591))
        self.textGeneratorLine3.setFrameShape(QtWidgets.QFrame.VLine)
        self.textGeneratorLine3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.textGeneratorLine4.setGeometry(QtCore.QRect(-3, 680, 1231, 20))
        self.textGeneratorLine4.setFrameShape(QtWidgets.QFrame.HLine)
        self.textGeneratorLine4.setFrameShadow(QtWidgets.QFrame.Sunken)

    def getFilePath(self):
        self.filePath = self.fileHandler.chooseFile()
        self.fileInputPathBox.setText(self.filePath)
        self.viewButton.setEnabled(True)    