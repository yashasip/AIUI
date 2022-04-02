from PyQt5 import QtCore, QtWidgets

from ui.ModelConfigGroup import ModelConfigGroup


class ConfigGroup:
    '''Config Group Ui Component and Functionality'''
    def __init__(self, parent) -> None:
        # sets up the config group box
        self.configGroupBox = QtWidgets.QGroupBox(parent)

        self.outcomeHeader = QtWidgets.QLabel(self.configGroupBox) # outcome header combo box
        self.outcomeHeaderComboBox = QtWidgets.QComboBox(self.configGroupBox)

        self.selectSheet = QtWidgets.QLabel(self.configGroupBox)  # select sheet combo box and label
        self.headersSelectionLabel = QtWidgets.QLabel(self.configGroupBox)
        self.headersListBox = QtWidgets.QListWidget(self.configGroupBox)

        self.selectSheetComboBox = QtWidgets.QComboBox(self.configGroupBox)

        self.modelConfig = ModelConfigGroup(self.configGroupBox) # Model Config group class

        self.setupConfigGroupUi() # calls setup ui component function

    def setupConfigGroupUi(self): # sets up ui components of Config Group
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

    def setupOutcomeHeaders(self, header_choices): # sets up all outcome headers based on list of header_choices
        self.outcomeHeaderComboBox.clear() # clears outcome header combo box values
        self.outcomeHeaderComboBox.addItems(header_choices)
        self.outcomeHeaderComboBox.setCurrentIndex(len(header_choices) - 1) # sets to last header column name 

    def setupHeadersListBox(self): # sets all header values based on outcomeHeadersComboBoxValues
        headersList = [
            self.outcomeHeaderComboBox.itemText(i)
            for i in range(self.outcomeHeaderComboBox.count())
        ]

        if not headersList:  # if no items, headersListBox is not updated
            return

        self.headersListBox.clear() # clear all previous values
        headersList.remove(self.outcomeHeaderComboBox.currentText())
        self.headersListBox.addItems(headersList) # insert new values

    def setupSelectSheetComboBox(self, sheetNames):
        self.selectSheetComboBox.clear()
        self.selectSheetComboBox.addItems(sheetNames)

    def getSelectedHeaders(self): # gets all the selected headers as a list of of strings and returns it
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
