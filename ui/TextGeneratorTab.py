from PyQt5 import QtCore, QtWidgets

from handle.FileHandle import FileHandle
from handle.TextDataFileHandle import TextDataFileHandle
from logic.TextGenerator import TextGenerator

class TextGeneratorTab():
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()

        self.textGeneratorFrame = QtWidgets.QFrame(self.tab)
        self.textGeneratorSelectorFrame = QtWidgets.QFrame(self.textGeneratorFrame)

        self.fileLabel = QtWidgets.QLabel(self.textGeneratorSelectorFrame)
        self.fileInputPathBox = QtWidgets.QLineEdit(self.textGeneratorSelectorFrame)
        self.chooseFileButton = QtWidgets.QPushButton(self.textGeneratorSelectorFrame)
        self.loadModelBtn = QtWidgets.QPushButton(self.textGeneratorSelectorFrame)
        self.viewButton = QtWidgets.QPushButton(self.textGeneratorSelectorFrame)

        self.configGroupBox = QtWidgets.QGroupBox(self.textGeneratorFrame)

        self.startFromLabel = QtWidgets.QLabel(self.configGroupBox)
        self.fromPageSpinBox = QtWidgets.QSpinBox(self.configGroupBox)

        self.epochsSpinBox = QtWidgets.QSpinBox(self.configGroupBox)
        self.epochsLabel = QtWidgets.QLabel(self.configGroupBox)
        
        self.temperatureLabel = QtWidgets.QLabel(self.configGroupBox)
        self.temperatureSpinBox = QtWidgets.QDoubleSpinBox(self.configGroupBox)

        self.optimizerLabel = QtWidgets.QLabel(self.configGroupBox)
        self.optimizerComboBox = QtWidgets.QComboBox(self.configGroupBox)
        self.optimizerComboBox.addItems(['Adam','Adagrad','Adadelta','Adamax','Ftrl','Nadam','SGD','RMSprop'])
        
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
        self.fileInputPathBox.textChanged.connect(self.setupConfigGroup)

        self.fileLabel.setGeometry(QtCore.QRect(230, 20, 31, 31))
        self.fileLabel.setText("File:")

        self.chooseFileButton.setGeometry(QtCore.QRect(510, 60, 93, 31))
        self.chooseFileButton.setText("Choose File")
        self.chooseFileButton.clicked.connect(self.getFilePath)

        self.viewButton.setEnabled(False)
        self.viewButton.setGeometry(QtCore.QRect(610, 60, 93, 31))
        self.viewButton.setText("View")
        self.viewButton.clicked.connect(self.fileHandler.viewFile)

        self.loadModelBtn.setGeometry(QtCore.QRect(710, 60, 93, 31))
        self.loadModelBtn.setText("Load Model")
        self.loadModelBtn.clicked.connect(self.loadExistingModel)

        self.textGeneratorLine1.setGeometry(QtCore.QRect(0, 90, 1221, 20))
        self.textGeneratorLine1.setFrameShape(QtWidgets.QFrame.HLine)
        self.textGeneratorLine1.setFrameShadow(QtWidgets.QFrame.Sunken)


        self.configGroupBox.setGeometry(QtCore.QRect(10, 100, 541, 570))
        self.configGroupBox.setTitle("Config")

        self.fromPageSpinBox.setGeometry(QtCore.QRect(160, 50, 81, 31))

        self.startFromLabel.setGeometry(QtCore.QRect(30, 45, 95, 45))
        self.startFromLabel.setText("Start From Page")

        self.batchSizeLabel = QtWidgets.QLabel(self.configGroupBox)
        self.epochsSpinBox.setGeometry(QtCore.QRect(160, 120, 81, 31))
        self.epochsSpinBox.setMaximum(1000)
        self.epochsSpinBox.setMinimum(1)
        self.epochsSpinBox.setValue(1)

        self.epochsLabel.setGeometry(QtCore.QRect(30, 120, 71, 31))
        self.epochsLabel.setText("Epochs")

        self.optimizerLabel.setGeometry(QtCore.QRect(30, 190, 61, 31))
        self.optimizerLabel.setText("Optimizer")

        self.optimizerComboBox.setGeometry(QtCore.QRect(160, 190, 181, 31))

        self.temperatureLabel.setGeometry(QtCore.QRect(30, 260, 91, 31))

        self.temperatureSpinBox.setGeometry(QtCore.QRect(160, 260, 61, 31))
        self.temperatureSpinBox.setMaximum(1.0)
        self.temperatureSpinBox.setProperty("value", 0.5)
        self.temperatureSpinBox.setMinimum(0.01)
        self.temperatureSpinBox.setMaximum(1)
        self.temperatureSpinBox.setSingleStep(0.1)
        self.temperatureLabel.setText("Temperature")

        self.sequenceLengthLabel.setGeometry(QtCore.QRect(30, 330, 111, 31))
        self.sequenceLengthLabel.setText("Sequence Length")

        self.batchSizeLabel.setGeometry(QtCore.QRect(30, 400, 71, 31))
        self.batchSizeLabel.setText("Batch Size")

        self.trainButton.setGeometry(QtCore.QRect(220, 470, 111, 31))
        self.trainButton.setText("Train")
        self.trainButton.clicked.connect(self.trainModel)

        self.saveModelButton.setEnabled(False)
        self.saveModelButton.setGeometry(QtCore.QRect(410, 530, 111, 31))
        self.saveModelButton.setText("Save Model")
        self.saveModelButton.clicked.connect(self.saveModel)
        self.saveModelButton.clicked.connect(self.saveNewModel)

        self.textGeneratorLine2.setGeometry(QtCore.QRect(0, 510, 551, 16))
        self.textGeneratorLine2.setFrameShape(QtWidgets.QFrame.HLine)
        self.textGeneratorLine2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.modelNameLabel.setGeometry(QtCore.QRect(10, 530, 321, 31))
        self.modelNameLabel.setText("Model Name:")

        self.sequenceLengthSpinBox.setGeometry(QtCore.QRect(160, 330, 111, 31))
        self.sequenceLengthSpinBox.setProperty("value", 100)
        self.sequenceLengthSpinBox.setMaximum(1000)
        self.sequenceLengthSpinBox.setMinimum(100)

        self.batchSizeSpinBox.setGeometry(QtCore.QRect(160, 400, 111, 31))
        self.batchSizeSpinBox.setProperty("value", 64)
        self.batchSizeSpinBox.setMinimum(64)
        self.batchSizeSpinBox.setMaximum(512)


        self.typeSpaceBoxFrame.setGeometry(QtCore.QRect(570, 100, 651, 570))
        self.typeSpaceBoxFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.typeSpaceBoxFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.typeSpaceBox.setGeometry(QtCore.QRect(10, 30, 631, 490))
        self.typeSpaceBox.setPlaceholderText("Start Typing Here")

        self.generateButton.setGeometry(QtCore.QRect(230, 528, 93, 31))
        self.generateButton.setText("Generate")
        self.generateButton.clicked.connect(self.predictText)

        self.typeSpaceLabel.setGeometry(QtCore.QRect(10, 0, 81, 31))
        self.typeSpaceLabel.setText("Type Space")

        self.saveButton.setGeometry(QtCore.QRect(330, 528, 93, 31))
        self.saveButton.setText("Save")
        self.saveButton.clicked.connect(self.saveTextDataFile)

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


    def setupConfigGroup(self):
        self.filePath = self.fileInputPathBox.text()
        self.fileInputPathBox.setText(self.filePath)
        self.chosenDataFile = TextDataFileHandle(self.filePath)
        if self.chosenDataFile.fileType == 'docx':
            self.startFromLabel.setDisabled(True)
            self.fromPageSpinBox.setDisabled(True)
        else:
            self.startFromLabel.setEnabled(True)
            self.fromPageSpinBox.setEnabled(True)

    def trainModel(self):
        self.textGenerator = TextGenerator(fileData = self.chosenDataFile.readTextDataFile(),
        epochsCount=self.epochsSpinBox.value(),
        optimizer=self.optimizerComboBox.currentText(),
        temperature=self.temperatureSpinBox.value(),
        sequenceLength=self.sequenceLengthSpinBox.value(),
        batchSize=self.batchSizeSpinBox.value())
        self.textGenerator.setupModel()
        self.saveModelButton.setEnabled(True)


    def predictText(self):
        if self.typeSpaceBox.toPlainText() == '':
            return

        generatedText = self.textGenerator.generateText(self.typeSpaceBox.toPlainText())
        self.typeSpaceBox.setPlainText(generatedText)

    def saveModel(self):
        self.textGenerator.saveModel()

    def loadExistingModel(self):
        self.loadModelHandle = FileHandle(self.textGeneratorFrame,fileFilter='Model (*.pb)')
        self.loadModelPath = self.loadModelHandle.openDirectory()
        if not self.loadModelPath:
            return 
        self.textGenerator = TextGenerator(generationType='LOAD')
        self.textGenerator.loadModel(self.loadModelPath)

    def saveTextDataFile(self):
        pathObj = self.fileHandler.saveFile(
            "*.docx" 
        )
        savePath = pathObj[0]
        if not savePath:
            return

        self.chosenDataFile.saveTextDataFile(savePath, self.typeSpaceBox.toPlainText())


    def saveNewModel(self):
        self.textGenerator.saveModel()

