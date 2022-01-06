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

    def setupXL(self):
        self.file = openpyxl.load_workbook(self.filePath)
        self.sheetNames = self.file.sheetnames

    def setupCSV(self):
        self.file = csv.DictReader(open(self.filePath))
        self.headers = self.setupHeaders(self.file.fieldnames)

    def setupXL(self):
        self.file = openpyxl.load_workbook(self.filePath)
        self.sheetNames = self.file.sheetnames
        self.sheet = self.file.active
        self.headers = ['a','b']

    def setupHeaders(self, headerRow):
        for header in headerRow:
            if header.isdecimal():
                return [f"Header {chr(65+i)}" for i in range(len(headerRow))]
        return headerRow



