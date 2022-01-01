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
        self.predictBtn = QtWidgets.QPushButton("Predict",self.tableLayout)
        self.saveBtn = QtWidgets.QPushButton("Save",self.tableLayout)
        self.tableButtonSpacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tableButtonSpacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        # User Defined Components
        self.fileHandler = BinaryClassifierInput(self.binaryTabFrame)
        self.config = ConfigGroup(parent=self.horizontalLayoutWidget)
        self.inputTable = DataTable(self.tableLayout)

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

        self.fileHandler.filePathInputBox.textChanged.connect(self.setupFunctionalComponents)
        self.config.headersListBox.itemSelectionChanged.connect(lambda: self.inputTable.setupTable(list(self.config.headersListBox.selectedItems()),self.config.outcomeHeaderComboBox.currentText()))
        self.config.outcomeHeaderComboBox.currentTextChanged.connect(lambda: self.inputTable.setupTable(list(self.config.headersListBox.selectedItems()),self.config.outcomeHeaderComboBox.currentText()))
        self.config.modelConfig.trainButton.clicked.connect(self.trainModel)
        self.predictBtn.clicked.connect(self.prediction)

        
    def setupFunctionalComponents(self):
        self.chosenFile = DataRecordFile(self.fileHandler.filePath)
        self.config.setupOutcomeHeaders(self.chosenFile.headers)
        self.config.setupHeadersListBox()
        self.inputTable.table.setEnabled(True)

    
    def trainModel(self):
        self.predictor = DataPredictor(self.chosenFile,list(self.config.headersListBox.selectedItems()), self.config.outcomeHeaderComboBox.currentText(), self.config.modelConfig.epochsSpinBox.value())

        self.predictor.trainModel()

    def prediction(self):
        predictions = self.predictor.predict(self.inputTable.getTableData())
        self.inputTable.setResultCells(predictions)
