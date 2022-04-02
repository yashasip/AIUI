from PyQt5 import QtCore, QtWidgets


class DataTable:
    '''Sets up Data Table Ui Widget
    parent: takes parent widget'''
    def __init__(self, parent) -> None:
        self.table = QtWidgets.QTableWidget(parent) # table
        self.addRowBtn = QtWidgets.QPushButton("+",self.table) # add and remove buttons
        self.deleteRowBtn = QtWidgets.QPushButton("-",self.table)
        self.setupDataTableWidgets() # sets up Data Table widgets

    def setupDataTableWidgets(self): # sets all data table widgets
        self.table.setDisabled(True)
        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(['Header A'])
        self.addRowBtn.setGeometry(QtCore.QRect(525, 440, 40, 40))
        self.addRowBtn.clicked.connect(self.addRow)
        self.deleteRowBtn.setGeometry(QtCore.QRect(475, 440, 40, 40))
        self.deleteRowBtn.setHidden(True)
        self.deleteRowBtn.clicked.connect(self.deleteRow)


    def setupTable(self, selectedItems, outcomeHeader): # setup table based on the selected headers
        self.table.clear() # clears all previous inputs
        self.headers = selectedItems + [outcomeHeader] # append all header values

        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents) # resizes columns according to values
        self.table.resizeColumnsToContents()

        self.setupTableCells() # sets up all the table cells

    
    def setupTableCells(self): # sets up all cells in the table
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                if self.table.item(row,column) is None:
                    self.table.setItem(row,column, QtWidgets.QTableWidgetItem()) # setup the cell

    def addRow(self): # adds a row to table
        self.deleteRowBtn.setHidden(False) # set hidden when table row count is 1
        self.table.setRowCount(self.table.rowCount() + 1)
        self.setupTableCells()

    def deleteRow(self):  # deletes row when table count > 1
        if self.table.rowCount() == 1:
            self.deleteRowBtn.setHidden(True) # hide when table is 1 to resstrict from further deletion
            return

        self.table.setRowCount(self.table.rowCount() - 1)

    def containsEmptyCell(self): # returns True if empty cell found, does not consider the last header
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                if column == self.table.columnCount() - 1:
                    continue
                if not self.table.item(row,column).text():
                    return True

        return False

    def getTableData(self, extractOutcomeHeader = False): # gets all table data, option to extract last header cell values
        tableData = []
        for row in range(self.table.rowCount()):
            rowData = []
            for column in range(self.table.columnCount()):
                if not extractOutcomeHeader and column == self.table.columnCount() - 1: # extracts table outcome header data only when required
                    continue
                rowData.append(float(self.table.item(row,column).text()))
            
            tableData.append(rowData) # appends data to the list
        return tableData

    def setResultCells(self, predictions): # sets all last header cell values
        column = self.table.columnCount() - 1 # gets last column value


        for row in range(self.table.rowCount()):
            self.table.item(row,column).setText(str(predictions[row]))
    
        #Resizing column everytime its updated
        self.table.resizeColumnsToContents()