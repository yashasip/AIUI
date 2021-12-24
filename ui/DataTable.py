from PyQt5 import QtCore, QtGui, QtWidgets


class DataTable:
    def __init__(self, parent) -> None:
        self.table = QtWidgets.QTableWidget(parent)
        self.table.setEnabled(False)
        self.table.setColumnCount(8)
        self.table.setRowCount(24)

        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()

        self.table.setHorizontalHeaderItem(7, item)

        # item row definition
        item = self.table.verticalHeaderItem(0)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(0)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(2)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(3)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(4)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(5)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(6)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(7)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(8)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(9)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(10)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(11)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(12)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(13)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(14)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(15)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(16)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(17)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(18)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(19)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(20)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(21)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(22)
        item.setText("New Row")
        item = self.table.verticalHeaderItem(23)
        item.setText("New Row")

        # item column definition
        item = self.table.horizontalHeaderItem(0)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(1)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(2)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(3)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(4)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(5)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(6)
        item.setText("New Column")
        item = self.table.horizontalHeaderItem(7)
        item.setText("New Column")
