import csv
import openpyxl



class DataRecordFile:
    def __init__(self, filePath) -> None:
        self.filePath = filePath
        self.fileType = self.getFileType()
        self.sheetNames=[]
        self.setupFile()

    def getFileType(self):
        for index, character in enumerate(self.filePath[::-1]):
            if character == ".":
                return self.filePath[-index:].lower()

    def setupFile(self):
        if self.fileType in ["xlsx", "xlsm", "xlsb", "xls"]:
            self.setupXL()
        else:
            self.setupCSV()


    def setupCSV(self):
        self.file = csv.DictReader(open(self.filePath))
        self.headers = self.setupHeaders(self.file.fieldnames)

    def setupXL(self):
        self.file = openpyxl.load_workbook(self.filePath)
        self.sheetNames = self.file.sheetnames
        self.currentSheet = self.file[self.sheetNames[0]]
        self.headers = self.setupHeaders(self.getHeadersXL())

    def setupHeaders(self, headerRow):
        for header in headerRow:
            if self.isNumber(header):
                return [f"Header {chr(65+i)}" for i in range(len(headerRow))]
        return headerRow

    def getHeadersXL(self):
        return [self.currentSheet.cell(row=1,column= column).value for column in range(1, self.currentSheet.max_column+1)]

    def changeSheetXL(self, changedSheet):
        self.currentSheet = self.file[changedSheet]
        self.headers = self.getHeadersXL() # check if required

    @staticmethod
    def isNumber(string):
        decimalParts = string.split('.')
        if len(decimalParts) > 2:
            return False
        for number in decimalParts:
            if not number.isdecimal():
                return False
        
        return True

