from PyQt5 import QtCore, QtGui, QtWidgets

from ui.FileHandle import FileHandle
from ui.ConfigGroup import ConfigGroup
from ui.DataTable import DataTable


class BinaryClassifierTab:
    def __init__(self) -> None:
        self.tab = QtWidgets.QWidget()

        self.tabLayout = QtWidgets.QWidget(self.tab)
        self.tabLayout.setContentsMargins(0, 0, 0, 0)
        self.tabLayout.setGeometry(QtCore.QRect(19, 9, 1211, 661))
        self.binaryInnerTabLayout = QtWidgets.QVBoxLayout(self.tabLayout)
        self.binaryInnerTabLayout.setContentsMargins(0, 0, 0, 0)

        self.binaryTabFrame = QtWidgets.QFrame(self.tabLayout)
        self.binaryTabFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.binaryTabFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        # File, File Input Handler
        self.FileHandler = FileHandle(self.binaryTabFrame)

        # Config box layout
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.binaryTabFrame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 581, 561))
        self.horizontalLayoutWidget.setContentsMargins(0, 0, 0, 0)

        self.ConfigLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ConfigLayout.setContentsMargins(0, 0, 0, 0)

        # Config Box
        self.Config = ConfigGroup(parent=self.horizontalLayoutWidget)
        self.ConfigLayout.addWidget(self.Config.ConfigGroupBox)

        # Table Layout
        self.tableLayout = QtWidgets.QWidget(self.binaryTabFrame)
        self.tableLayout.setGeometry(QtCore.QRect(609, 99, 601, 561))

        self.inputTableLayout = QtWidgets.QVBoxLayout(self.tableLayout)
        self.inputTableLayout.setContentsMargins(0, 0, 0, 0)
        
        self.tableHorizontalButtonsLayout = QtWidgets.QHBoxLayout(self.tableLayout)

        self.tableButtonSpacer1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tableButtonSpacer2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        self.tableHorizontalButtonsLayout.addItem(self.tableButtonSpacer1)

        self.saveBtn = QtWidgets.QPushButton("Save",self.tableLayout)
        self.saveBtn.setGeometry(QtCore.QRect(640, 695, 101, 28))
        self.tableHorizontalButtonsLayout.addWidget(self.saveBtn)

        self.predictBtn = QtWidgets.QPushButton("Predict",self.tableLayout)
        self.predictBtn.setGeometry(QtCore.QRect(640, 695, 101, 28))
        self.tableHorizontalButtonsLayout.addWidget(self.predictBtn)

        self.tableHorizontalButtonsLayout.addItem(self.tableButtonSpacer2)

        # input table set
        self.inputTable = DataTable(self.tableLayout)
        self.inputTableLayout.addWidget(self.inputTable.inputDataTable)
        self.inputTableLayout.addLayout(self.tableHorizontalButtonsLayout)
        self.binaryInnerTabLayout.addWidget(self.binaryTabFrame)
