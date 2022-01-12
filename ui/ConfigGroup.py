from PyQt5 import QtCore, QtGui, QtWidgets

from ui.ModelConfigGroup import ModelConfigGroup


class ConfigGroup:
    def __init__(self, parent) -> None:
        self.configGroupBox = QtWidgets.QGroupBox(parent)

        self.outcomeHeader = QtWidgets.QLabel(self.configGroupBox)
        self.outcomeHeaderComboBox = QtWidgets.QComboBox(self.configGroupBox)

        self.selectSheet = QtWidgets.QLabel(self.configGroupBox)
        self.headersSelectionLabel = QtWidgets.QLabel(self.configGroupBox)
        self.headersListBox = QtWidgets.QListWidget(self.configGroupBox)

        self.selectSheetComboBox = QtWidgets.QComboBox(self.configGroupBox)

        self.modelConfig = ModelConfigGroup(self.configGroupBox)

        self.setupConfigGroupUi()

    def setupConfigGroupUi(self):
        self.configGroupBox.setTitle("Config")
        self.configGroupBox.setDisabled(True)

        self.outcomeHeader.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.outcomeHeader.setText("Outcome Header")

        self.outcomeHeaderComboBox.setGeometry(QtCore.QRect(130, 30, 171, 31))
        self.outcomeHeaderComboBox.currentTextChanged.connect(self.setupHeadersListBox)

        self.headersSelectionLabel.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.headersSelectionLabel.setText("Select Headers")

        self.headersListBox.setGeometry(QtCore.QRect(20, 102, 521, 81))
        self.headersListBox.setSelectionMode(QtWidgets.QListWidget.MultiSelection)

        self.selectSheet.setGeometry(QtCore.QRect(310, 30, 81, 31))
        self.selectSheet.setText("Select Sheet")

        self.selectSheetComboBox.setGeometry(QtCore.QRect(390, 30, 171, 31))

    def setupOutcomeHeaders(self, header_choices):
        self.outcomeHeaderComboBox.clear()
        self.outcomeHeaderComboBox.addItems(header_choices)
        self.outcomeHeaderComboBox.setCurrentIndex(len(header_choices) - 1) # sets to last header column name 

    def setupHeadersListBox(self): # sets all header values based on outcomeHeadersComboBoxValues
        headersList = [
            self.outcomeHeaderComboBox.itemText(i)
            for i in range(self.outcomeHeaderComboBox.count())
        ]

        if not headersList:  # if no items, headersListBox is not updated
            return

        self.headersListBox.clear()
        headersList.remove(self.outcomeHeaderComboBox.currentText())
        self.headersListBox.addItems(headersList)

    def setupSelectSheetComboBox(self, sheetNames):
        self.selectSheetComboBox.clear()
        self.selectSheetComboBox.addItems(sheetNames)

    def getSelectedHeaders(self):
        selectedHeaders = []
        for i in range(self.headersListBox.count()):
            if self.headersListBox.item(i).isSelected():
                selectedHeaders += [self.headersListBox.item(i).text()]

        return selectedHeaders

    def getSelectedHeadersIndex(self): # returns selectedHeaders index list which is in the ascending order
        selectedHeaders = []
        for i in range(self.headersListBox.count()):
            if self.headersListBox.item(i).isSelected():
                selectedHeaders += [i]

        return selectedHeaders

    def toggleModelConfig(self): # toggles between disable and enable states 
        if len(self.headersListBox.selectedIndexes()) < 1:
            self.modelConfig.ModelConfigBox.setDisabled(True)
            return

        self.modelConfig.ModelConfigBox.setEnabled(True)
