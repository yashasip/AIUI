from PyQt5 import QtCore, QtGui, QtWidgets

from ui.ModelConfigGroup import ModelConfigGroup


class ConfigGroup:
    def __init__(self, parent) -> None:
        self.ConfigGroupBox = QtWidgets.QGroupBox(parent)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.outcomeHeader = QtWidgets.QLabel(self.ConfigGroupBox)
        self.outcomeHeaderComboBox = QtWidgets.QComboBox(self.ConfigGroupBox)

        self.attributesListView = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.attributesCheckBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)

        self.attributesScrollArea = QtWidgets.QScrollArea(self.ConfigGroupBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.selectSheet = QtWidgets.QLabel(self.ConfigGroupBox)
        self.attributeSelectionLabel = QtWidgets.QLabel(self.ConfigGroupBox)
        self.selectSheetComboBox = QtWidgets.QComboBox(self.ConfigGroupBox)

        self.ModelConfig = ModelConfigGroup(self.ConfigGroupBox)

        self.setupConfigGroupUi()

    def setupConfigGroupUi(self):
        self.ConfigGroupBox.setTitle("Config")

        self.outcomeHeader.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.outcomeHeader.setText("Outcome Header")

        self.outcomeHeaderComboBox.setGeometry(QtCore.QRect(130, 30, 171, 31))

        self.attributeSelectionLabel.setGeometry(QtCore.QRect(20, 70, 111, 31))
        self.attributeSelectionLabel.setText("Attributes Selection")

        self.attributesScrollArea.setWidgetResizable(True)
        self.attributesScrollArea.setGeometry(QtCore.QRect(20, 110, 521, 81))

        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 79))

        self.attributesListView.setGeometry(QtCore.QRect(10, 10, 501, 61))
        self.attributesCheckBox.setGeometry(QtCore.QRect(20, 20, 81, 20))
        self.attributesCheckBox.setText("CheckBox")

        self.checkBox_2.setGeometry(QtCore.QRect(20, 40, 81, 20))
        self.checkBox_2.setText("CheckBox")

        self.attributesScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.selectSheet.setGeometry(QtCore.QRect(310, 30, 81, 31))
        self.selectSheet.setText("Select Sheet")

        self.selectSheetComboBox.setGeometry(QtCore.QRect(390, 30, 171, 31))
