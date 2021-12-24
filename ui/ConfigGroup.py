from PyQt5 import QtCore, QtGui, QtWidgets

from ui.ModelConfigGroup import ModelConfigGroup


class ConfigGroup:
    def __init__(self, parent) -> None:
        self.configGroupBox = QtWidgets.QGroupBox(parent)
        
        self.outcomeHeader = QtWidgets.QLabel(self.configGroupBox)
        self.outcomeHeaderComboBox = QtWidgets.QComboBox(self.configGroupBox)

        self.selectSheet = QtWidgets.QLabel(self.configGroupBox)
        self.attributeSelectionLabel = QtWidgets.QLabel(self.configGroupBox)
        self.selectSheetComboBox = QtWidgets.QComboBox(self.configGroupBox)

        self.modelConfig = ModelConfigGroup(self.configGroupBox)

        self.setupConfigGroupUi()

    def setupConfigGroupUi(self):
        self.configGroupBox.setTitle("Config")

        self.outcomeHeader.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.outcomeHeader.setText("Outcome Header")

        self.outcomeHeaderComboBox.setGeometry(QtCore.QRect(130, 30, 171, 31))

        self.attributeSelectionLabel.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.attributeSelectionLabel.setText("Attributes Selection")

        self.selectSheet.setGeometry(QtCore.QRect(310, 30, 81, 31))
        self.selectSheet.setText("Select Sheet")

        self.selectSheetComboBox.setGeometry(QtCore.QRect(390, 30, 171, 31))

    def setupOutcomeHeaders(self,header_choices):
        self.outcomeHeaderComboBox.clear()
        self.outcomeHeaderComboBox.addItems(header_choices)

    

