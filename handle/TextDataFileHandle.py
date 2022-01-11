import docx
import PyPDF2
import requests


class TextDataFileHandle:
    def __init__(self, filePath) -> None:
        self.filePath = filePath
        self.fileType = self.getFileType()

        self.setupTextDataFile()

    def getFileType(self):
        for index, character in enumerate(self.filePath[::-1]):
            if character == ".":
                return self.filePath[-index:].lower()

    def setupTextDataFile(self):
        if self.filePath.startswith("https://") or self.filePath.startswith("http://"):
            self.scrapePdf()
            self.filePath = "inputPDF.pdf"
        if self.fileType == "pdf":
            pdfFile = open(self.filePath, "rb")
            self.reader = PyPDF2.PdfFileReader(pdfFile)
            self.pageCount = self.reader.numPages

    def readTextDataFile(self):
        if self.fileType == "pdf":
            textData = self.readPDF()
        elif self.fileType == "docx":
            textData = self.readDocx()
        return textData

    def readPDF(self, start=0):
        pdfData = ""
        for i in range(start, self.pageCount):
            page = self.reader.getPage(i)
            pdfData = pdfData + str(page.extractText())

        return pdfData

    def readDocx(self, start=0):
        doc = docx.Document(self.filePath)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return "\n".join(fullText)

    def scrapePdf(self):
        html = requests.get(self.filePath, stream=True)
        file = open("inputPDF.pdf", "wb")
        for chunk in html.iter_content(1000):
            file.write(chunk)
        file.close()

    def saveTextDataFile(self,path, content):
        newDoc = docx.Document()
        newDoc.add_paragraph(content)
        newDoc.save(path)        