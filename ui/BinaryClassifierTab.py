import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from handle.DataRecordFile import DataRecordFile
from logic.DataPredictor import DataPredictor

from ui.BinaryClassifierInput import BinaryClassifierInput
from ui.ConfigGroup import ConfigGroup
from ui.DataTable import DataTable


class BinaryClassifierTab:
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()
        self.tabLayout = QtWidgets.QWidget(self.tab)

        self.binaryInnerTabLayout = QtWidgets.QVBoxLayout(self.tabLayout)
        self.binaryTabFrame = QtWidgets.QFrame(self.tabLayout)

        # config components
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.binaryTabFrame)
        self.configLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)

        # Table & related Components
        self.tableLayout = QtWidgets.QWidget(self.binaryTabFrame)
        self.inputTableLayout = QtWidgets.QVBoxLayout(self.tableLayout)
        self.tableHorizontalButtonsLayout = QtWidgets.QHBoxLayout(self.tableLayout)
        self.predictBtn = QtWidgets.QPushButton("Predict", self.tableLayout)
        self.saveBtn = QtWidgets.QPushButton("Save", self.tableLayout)
        self.tableButtonSpacer1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.tableButtonSpacer2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )

        # User Defined Components
        self.binaryFileInputHandle = BinaryClassifierInput(self.binaryTabFrame)
        self.config = ConfigGroup(parent=self.horizontalLayoutWidget)
        self.inputTable = DataTable(self.tableLayout)

        self.chosenFile = None

        self.setupBinaryClassifierTab()

    def setupBinaryClassifierTab(self):
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.tabLayout.setGeometry(QtCore.QRect(19, 9, 1199, 651))
        self.binaryInnerTabLayout.setContentsMargins(0, 0, 0, 0)

        self.binaryTabFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binaryTabFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        # config box layout
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 78, 581, 561))
        self.horizontalLayoutWidget.setContentsMargins(0, 0, 0, 0)

        self.configLayout.setContentsMargins(0, 0, 0, 0)

        # config Box
        self.configLayout.addWidget(self.config.configGroupBox)

        # Table Layout
        self.tableLayout.setGeometry(QtCore.QRect(609, 99, 580, 540))

        self.inputTableLayout.setContentsMargins(0, 0, 0, 0)

        self.tableHorizontalButtonsLayout.addItem(self.tableButtonSpacer1)
        self.tableHorizontalButtonsLayout.addWidget(self.predictBtn)

        self.tableHorizontalButtonsLayout.addWidget(self.saveBtn)
        self.tableHorizontalButtonsLayout.addItem(self.tableButtonSpacer2)

        # input table & related components set
        self.inputTableLayout.addWidget(self.inputTable.table)
        self.inputTableLayout.addLayout(self.tableHorizontalButtonsLayout)
        self.binaryInnerTabLayout.addWidget(self.binaryTabFrame)

        self.predictBtn.setDisabled(True)
        self.saveBtn.setDisabled(True)

        self.binaryFileInputHandle.filePathInputBox.textChanged.connect(
            self.setupFunctionalComponents
        )
        self.config.headersListBox.itemSelectionChanged.connect(
            lambda: self.inputTable.setupTable(
                self.config.getSelectedHeaders(),
                self.config.outcomeHeaderComboBox.currentText(),
            )
        )
        self.config.headersListBox.itemSelectionChanged.connect(
            self.config.toggleModelConfig
        )
        self.config.outcomeHeaderComboBox.currentTextChanged.connect(
            lambda: self.inputTable.setupTable(
                list(self.config.headersListBox.selectedItems()),
                self.config.outcomeHeaderComboBox.currentText(),
            )
        )
        self.config.modelConfig.trainButton.clicked.connect(self.trainModel)
        self.predictBtn.clicked.connect(self.prediction)
        self.config.selectSheetComboBox.currentTextChanged.connect(self.setupSheet)
        self.saveBtn.clicked.connect(self.saveDataRecordFile)

    def setupFunctionalComponents(self):
        self.config.configGroupBox.setEnabled(True)
        self.chosenFile = DataRecordFile(self.binaryFileInputHandle.filePath)
        if self.chosenFile.fileType == "csv":
            self.config.selectSheet.setHidden(True)
            self.config.selectSheetComboBox.setHidden(True)
        else:
            self.config.selectSheet.setVisible(True)
            self.config.selectSheetComboBox.setVisible(True)

        if self.chosenFile.fileType != "csv":
            self.config.setupselectSheetComboBox(self.chosenFile.sheetNames)
        self.config.setupOutcomeHeaders(self.chosenFile.headers)

    def trainModel(self):
        self.config.modelConfig.trainingLabel.setHidden(False)
        self.predictor = DataPredictor(
            dataRecord=self.chosenFile,
            selectedHeadersIndex=self.config.getSelectedHeadersIndex(),
            outcomeHeaderIndex=self.config.outcomeHeaderComboBox.currentIndex(),
            epochsCount=self.config.modelConfig.epochsSpinBox.value(),
            activationFunction=self.config.modelConfig.activationFunctionComboBox.currentText().lower(),
            optimizerType=self.config.modelConfig.optimizerComboBox.currentText(),
            scaling=self.config.modelConfig.scalingTypeGroup.checkedButton().text(),
        )

        self.config.modelConfig.trainingLabel.setHidden(True)
        self.predictor.trainModel()
        self.inputTable.table.setEnabled(True)
        self.predictBtn.setEnabled(True)
        self.saveBtn.setEnabled(True)

    def prediction(self):
        if self.inputTable.containsEmptyCell():
            return  # *** display dialog box
        tableData = self.inputTable.getTableData()
        predictions = self.predictor.predict(tableData)
        self.inputTable.setResultCells(predictions)

    def setupSheet(self):
        self.chosenFile.changeSheetXL(self.config.selectSheetComboBox.currentText())
        self.config.setupOutcomeHeaders(self.chosenFile.headers)

    def saveDataRecordFile(self):
        name = self.binaryFileInputHandle.fileHandler.saveFile(
            "*." + self.chosenFile.fileType
        )
        savePath = name[0]
        if not savePath:
            return

        self.chosenFile.saveDataRecordFile(savePath, self.inputTable.getTableData(extractOutcomeHeader=True))
        #add a save dialog box
