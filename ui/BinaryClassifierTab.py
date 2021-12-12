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

        # input table set
        self.inputTable = DataTable(self.tableLayout)
        self.inputTableLayout.addWidget(self.inputTable.inputDataTable)
        self.binaryInnerTabLayout.addWidget(self.binaryTabFrame)
