from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler


class DataPredictor:
    def __init__(
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

    def cleanData(self):  # works for selectedHeadersIndex only
        if self.dataRecord.fileType == "csv":
            self.data = self.dataRecord.cleanCsvData(
                self.selectedHeadersIndex + [self.outcomeHeaderIndex]
            )
        else:
            self.data = self.dataRecord.cleanXLData(
                self.selectedHeadersIndex + [self.outcomeHeaderIndex]
            )

        self.data = pd.DataFrame(self.data)

    def splitData(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.data[range(len(self.selectedHeadersIndex))],
            self.data[[len(self.selectedHeadersIndex)]],
            test_size=0.2,
            random_state=25,
        )  # headers shape size
        

    def ScaleData(self):
        if self.scaling == 'Standardization':
            self.std = StandardScaler().fit(self.x_train)
            self.x_train_scaled = pd.DataFrame(self.std.transform(self.x_train))
            self.x_test_scaled = pd.DataFrame(self.std.transform(self.x_test))
        else:
            self.norm = MinMaxScaler().fit(self.x_train)
            self.x_train_scaled = pd.DataFrame(self.norm.transform(self.x_train))
            self.x_test_scaled = pd.DataFrame(self.norm.transform(self.x_test))

    def buildModel(self):
        self.model = Sequential(
            [
                layers.Dense(
                    1,
                    input_shape=(len(self.selectedHeadersIndex),),
                    activation=self.activationFunction,
                    kernel_initializer="ones",
                    bias_initializer="zeros",
                )
            ]
        )  # input shape size

        self.model.compile(
            optimizer=self.optimizerType,
            loss="binary_crossentropy",
            metrics=["accuracy"],
        )

        self.model.fit(
            self.x_train_scaled, self.y_train, epochs=self.epochsCount
        )  # *** epochs as variable

    def evaluateModel(self):
        self.model.evaluate(self.x_test_scaled, self.y_test)

    def predict(self, inputData):
        inputData = pd.DataFrame(inputData)
        if self.scaling == 'Standardization':
            inputData = pd.DataFrame(self.std.transform(inputData))
        else:
            inputData = pd.DataFrame(self.norm.transform(inputData))

        predictions = self.model.predict(inputData)
        return [float(item) for item in list(predictions)]

    def trainModel(self):
        self.splitData()
        self.ScaleData()
        self.buildModel()
        self.evaluateModel()
