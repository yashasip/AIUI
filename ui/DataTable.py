from PyQt5 import QtCore, QtGui, QtWidgets


class DataTable:
    def __init__(self, parent) -> None:
        self.table = QtWidgets.QTableWidget(parent)
        self.addRowBtn = QtWidgets.QPushButton("+",self.table)
        self.deleteRowBtn = QtWidgets.QPushButton("-",self.table)
        self.setupDataTableWidgets()

    def setupDataTableWidgets(self):
        self.table.setDisabled(True)
        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['Header A'])
        self.addRowBtn.setGeometry(QtCore.QRect(525, 440, 40, 40))
        self.addRowBtn.clicked.connect(self.addRow)
        self.deleteRowBtn.setGeometry(QtCore.QRect(475, 440, 40, 40))
        self.deleteRowBtn.setHidden(True)
        self.deleteRowBtn.clicked.connect(self.deleteRow)


    def setupTable(self, selectedItems, outcomeHeader):
        self.headers = selectedItems + [outcomeHeader]

        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)


        self.setupTableCells()

    
    def setupTableCells(self):
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                if self.table.item(row,column) is None:
                    self.table.setItem(row,column, QtWidgets.QTableWidgetItem())

    def addRow(self):
        self.deleteRowBtn.setHidden(False)
        self.table.setRowCount(self.table.rowCount() + 1)
        self.setupTableCells()

    def deleteRow(self):
        if self.table.rowCount() == 1:
            self.deleteRowBtn.setHidden(True)
            return

        self.table.setRowCount(self.table.rowCount() - 1)

    def isTableDataValid(self):
        for row in range(self.table.rowCount()):
            rowData = []
            for column in range(self.table.columnCount()):
                if column == self.table.columnCount() - 1:
                    continue
                if not self.table.item(row,column).text():
                    return False

        return True

    def getTableData(self, extractOutcomeHeader = False):
        if not self.isTableDataValid():
            return # display invalid popup window

        tableData = []
        for row in range(self.table.rowCount()):
            rowData = []
            for column in range(self.table.columnCount()):
                if not extractOutcomeHeader and column == self.table.columnCount - 1:
                    continue
                rowData.append(int(self.table.item(row,column).text()))
            
            tableData.append(rowData)
        return tableData

    def setResultCells(self, predictions):
        column = self.table.columnCount() - 1


        for row in range(self.table.rowCount()):
            self.table.item(row,column).setText(str(predictions[row]))
    
        #RESIZING COLUMNS EVERYTIME ITS UPDATED
        self.table.resizeColumnsToContents()