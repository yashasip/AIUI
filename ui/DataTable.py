from PyQt5 import QtCore, QtGui, QtWidgets


class DataTable:
    def __init__(self, parent) -> None:
        self.table = QtWidgets.QTableWidget(parent)
        self.table.setEnabled(False)
        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['Header A'])

    def setupTable(self, selectedItems, outcomeHeader):
        self.headers = [item.text() for item in selectedItems] + [outcomeHeader]

        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)