from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class DataPredictor:
    '''Binary Classifier Model Creation'''
    def __init__( # set all model parameters based on user input through user interface
        self,
        dataRecord,
        selectedHeadersIndex,
        outcomeHeaderIndex,
        epochsCount=5000,
        optimizerType="adam",
        activationFunction="sigmoid",
        scaling='Normalization',
    ) -> None:
        self.dataRecord = dataRecord
        self.file = self.dataRecord.file

        self.selectedHeadersIndex = selectedHeadersIndex
        self.outcomeHeaderIndex = outcomeHeaderIndex
        self.epochsCount = epochsCount
        self.optimizerType = optimizerType
        self.activationFunction = activationFunction
        self.scaling = scaling

        self.cleanData()

    def cleanData(self):  # extract and clean data to be used to create a model
        if self.dataRecord.fileType == "csv":
            self.data = self.dataRecord.cleanCsvData(
                self.selectedHeadersIndex + [self.outcomeHeaderIndex]
            )
        else:
            self.data = self.dataRecord.cleanXLData(
                self.selectedHeadersIndex + [self.outcomeHeaderIndex]
            )

        self.data = pd.DataFrame(self.data)

    def splitData(self): # splits data for training and testing
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.data[range(len(self.selectedHeadersIndex))],
            self.data[[len(self.selectedHeadersIndex)]],
            test_size=0.2, # 20% of data is used for testing
            random_state=25,
        )  # headers shape size
        

    def ScaleData(self): # scales data extracted based of scaling type
        if self.scaling == 'Standardization':
            self.std = StandardScaler().fit(self.x_train)
            self.x_train_scaled = pd.DataFrame(self.std.transform(self.x_train))
            self.x_test_scaled = pd.DataFrame(self.std.transform(self.x_test))
        else:# defaults to normalization
            self.norm = MinMaxScaler().fit(self.x_train)
            self.x_train_scaled = pd.DataFrame(self.norm.transform(self.x_train))
            self.x_test_scaled = pd.DataFrame(self.norm.transform(self.x_test))

    def buildModel(self): # creates a model
        self.model = Sequential(
            [
                layers.Dense(
                    1,
                    input_shape=(len(self.selectedHeadersIndex),),
                    activation=self.activationFunction, # pass activation function
                    kernel_initializer="ones",
                    bias_initializer="zeros",
                )
            ]
        )  # input shape size

        self.model.compile( # compile the model
            optimizer=self.optimizerType,
            loss="binary_crossentropy",
            metrics=["accuracy"],
        )

        self.model.fit( # fit the model
            self.x_train_scaled, self.y_train, epochs=self.epochsCount
        ) 

    def evaluateModel(self): # evaluate model based on test results
        self.model.evaluate(self.x_test_scaled, self.y_test)

    def predict(self, inputData): # calculates the prediction
        inputData = pd.DataFrame(inputData) # convert to dataframe
        if self.scaling == 'Standardization': # scale the data based on scaling type
            inputData = pd.DataFrame(self.std.transform(inputData))
        else:
            inputData = pd.DataFrame(self.norm.transform(inputData))

        predictions = self.model.predict(inputData) # display predictions
        return [float(item) for item in list(predictions)]

    def trainModel(self): # train model, this method is called by other classes
        self.splitData()
        self.ScaleData()
        self.buildModel()
        self.evaluateModel()
