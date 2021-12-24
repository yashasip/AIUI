from PyQt5 import QtCore, QtGui, QtWidgets


class ModelConfigGroup:
    def __init__(self, parent) -> None:
        self.ModelConfigBox = QtWidgets.QGroupBox(parent)
        self.modelTrainProgressBar = QtWidgets.QProgressBar(self.ModelConfigBox)
        self.trainButton = QtWidgets.QPushButton(self.ModelConfigBox)
        self.epochsSpinBox = QtWidgets.QSpinBox(self.ModelConfigBox)
        self.EpochsLabel = QtWidgets.QLabel(self.ModelConfigBox)
        self.activationFunctionComboBox = QtWidgets.QComboBox(self.ModelConfigBox)
        self.activationFunctionLabel = QtWidgets.QLabel(self.ModelConfigBox)
        self.moreOptionsToolButton = QtWidgets.QToolButton(self.ModelConfigBox)
        self.LoadModelToolButton = QtWidgets.QToolButton(self.ModelConfigBox)
        self.optimizerLabel = QtWidgets.QLabel(self.ModelConfigBox)
        self.optimizerComboBox = QtWidgets.QComboBox(self.ModelConfigBox)
        self.normalizationRadioButton = QtWidgets.QRadioButton(self.ModelConfigBox)
        self.standardizationRadioButton = QtWidgets.QRadioButton(self.ModelConfigBox)
        self.scalingLabel = QtWidgets.QLabel(self.ModelConfigBox)

        self.setupModelConfigUi()

    def setupModelConfigUi(self):
        self.ModelConfigBox.setGeometry(QtCore.QRect(10, 210, 561, 341))
        self.ModelConfigBox.setTitle("Model Config")

        self.modelTrainProgressBar.setGeometry(QtCore.QRect(170, 270, 271, 23))
        self.modelTrainProgressBar.setProperty("value", 0)

        self.trainButton.setGeometry(QtCore.QRect(240, 300, 101, 28))
        self.trainButton.setText("Train")

        self.epochsSpinBox.setGeometry(QtCore.QRect(170, 40, 91, 31))

        self.EpochsLabel.setGeometry(QtCore.QRect(30, 40, 51, 31))
        self.EpochsLabel.setText("Epochs")

        self.activationFunctionComboBox.setGeometry(QtCore.QRect(170, 150, 231, 31))

        self.activationFunctionLabel.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.activationFunctionLabel.setText("Activation Function")
        self.activationFunctionComboBox.addItems(['Sigmoid','Relu','Softmax','Softplus','Softsign','Tanh','Selu','Elu','Exponential'])

        self.moreOptionsToolButton.setGeometry(QtCore.QRect(500, 20, 41, 41))
        self.moreOptionsToolButton.setText("...")

        self.LoadModelToolButton.setGeometry(QtCore.QRect(450, 20, 41, 41))
        self.LoadModelToolButton.setText("...")

        self.optimizerLabel.setGeometry(QtCore.QRect(30, 100, 61, 31))
        self.optimizerLabel.setText("Optimizer")

        self.optimizerComboBox.setGeometry(QtCore.QRect(170, 100, 231, 31))
        self.optimizerComboBox.addItems(['Adam','SGD','RMSprop','Adadelta','Adagrad','Adamax','Nadam','Ftrl'])

        self.normalizationRadioButton.setGeometry(QtCore.QRect(170, 210, 111, 21))
        self.normalizationRadioButton.setChecked(True)
        self.normalizationRadioButton.setText("Normalization")

        self.standardizationRadioButton.setText("Standardization")
        self.standardizationRadioButton.setGeometry(QtCore.QRect(290, 210, 121, 21))
        self.standardizationRadioButton.setChecked(False)
        self.standardizationRadioButton.setObjectName("standardizationRadioButton")

        self.scalingLabel.setGeometry(QtCore.QRect(30, 210, 61, 21))
        self.scalingLabel.setObjectName("scalingLabel")
        self.scalingLabel.setText("Scaling")
