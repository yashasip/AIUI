from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

class DataPredictor:
    def __init__(self, dataRecord, selectedHeaders, outcomeHeader, epochsCount=5000, optimizerType='adam', activationFunction='sigmoid', Scaling=None ) -> None:
        self.dataRecord = dataRecord
        self.file = self.dataRecord.file

        self.selectedHeaders = selectedHeaders
        self.outcomeHeader = outcomeHeader
        self.epochsCount = epochsCount
        self.optimizerType=optimizerType
        self.activationFunction = activationFunction

        self.cleanData()

    def cleanData(self): # works for selectedHeaders only 
        if self.dataRecord.fileType == 'csv':
            self.cleanCsvData() 
        else:
            self.cleanXLData()

        self.data = pd.DataFrame(self.data)

    def cleanCsvData(self):
        self.data = []
        for row in self.file: # first row is missed if no header
            rowData = []
            for item in row.items():
                rowData += [float(item[1])]
            self.data+=[rowData]

    def cleanXLData():
        pass

    def splitScaleData(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data[range(len(self.selectedHeaders))],self.data[[len(self.selectedHeaders)]],test_size=0.2,random_state=25) # headers shape size
        self.norm = MinMaxScaler().fit(self.x_train)
        self.x_train_scaled = pd.DataFrame(self.norm.transform(self.x_train))
        self.x_test_scaled = pd.DataFrame(self.norm.transform(self.x_test))


    def buildModel(self):
        self.model = Sequential([layers.Dense(1,input_shape=(len(self.selectedHeaders),),activation=self.activationFunction, kernel_initializer='ones',bias_initializer='zeros')]) # input shape size

        self.model.compile(optimizer=self.optimizerType, loss='binary_crossentropy', metrics=['accuracy'])

        self.model.fit(self.x_train_scaled,self.y_train, epochs=self.epochsCount) # *** epochs as variable


    def evaluateModel(self):
        print(self.model.evaluate(self.x_test_scaled,self.y_test))

    def predict(self, inputData):
        inputData = pd.DataFrame(inputData)
        inputData = pd.DataFrame(self.norm.transform(inputData))
        predictions = self.model.predict(inputData)
        return [float(item) for item in list(predictions)]

    
    def trainModel(self):
        self.splitScaleData()
        self.buildModel()
        self.evaluateModel()