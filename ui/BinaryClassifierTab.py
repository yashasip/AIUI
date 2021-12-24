from PyQt5 import QtCore, QtGui, QtWidgets

from ui.FileHandle import FileHandle
from ui.ConfigGroup import ConfigGroup
from ui.DataTable import DataTable


class BinaryClassifierTab:
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()
        self.tabLayout = QtWidgets.QWidget(self.tab)

        self.binaryInnerTabLayout = QtWidgets.QVBoxLayout(self.tabLayout)
        self.binaryTabFrame = QtWidgets.QFrame(self.tabLayout)

        # Config components
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.binaryTabFrame)
        self.ConfigLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        
        # Table & related Components
        self.tableLayout = QtWidgets.QWidget(self.binaryTabFrame)
        self.inputTableLayout = QtWidgets.QVBoxLayout(self.tableLayout)
        self.tableHorizontalButtonsLayout = QtWidgets.QHBoxLayout(self.tableLayout)
        self.predictBtn = QtWidgets.QPushButton("Predict",self.tableLayout)
        self.saveBtn = QtWidgets.QPushButton("Save",self.tableLayout)
        self.tableButtonSpacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tableButtonSpacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        # User Defined Components
        self.FileHandler = FileHandle(self.binaryTabFrame)
        self.Config = ConfigGroup(parent=self.horizontalLayoutWidget)
        self.inputTable = DataTable(self.tableLayout)

        self.setupBinaryClassifierTab()

    def setupBinaryClassifierTab(self):
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.tabLayout.setGeometry(QtCore.QRect(19, 9, 1199, 651))
        self.binaryInnerTabLayout.setContentsMargins(0, 0, 0, 0)

        self.binaryTabFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binaryTabFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Config box layout
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 78, 581, 561))
        self.horizontalLayoutWidget.setContentsMargins(0, 0, 0, 0)

        self.ConfigLayout.setContentsMargins(0, 0, 0, 0)

        # Config Box
        self.ConfigLayout.addWidget(self.Config.ConfigGroupBox)

        # Table Layout
        self.tableLayout.setGeometry(QtCore.QRect(609, 99, 580, 540))

        self.inputTableLayout.setContentsMargins(0, 0, 0, 0)

        self.tableHorizontalButtonsLayout.addItem(self.tableButtonSpacer1)
        self.tableHorizontalButtonsLayout.addWidget(self.predictBtn)

        self.tableHorizontalButtonsLayout.addWidget(self.saveBtn)
        self.tableHorizontalButtonsLayout.addItem(self.tableButtonSpacer2)

        # input table & related components set
        self.inputTableLayout.addWidget(self.inputTable.inputDataTable)
        self.inputTableLayout.addLayout(self.tableHorizontalButtonsLayout)
        self.binaryInnerTabLayout.addWidget(self.binaryTabFrame)
