from PyQt5 import QtCore, QtWidgets


class ModelConfigGroup:
    '''Model Config Widgets available '''
    def __init__(self, parent) -> None:
        self.ModelConfigBox = QtWidgets.QGroupBox(parent) # Main group box
        self.trainButton = QtWidgets.QPushButton(self.ModelConfigBox)
        self.epochsSpinBox = QtWidgets.QSpinBox(self.ModelConfigBox) # set epochs spin box
        self.EpochsLabel = QtWidgets.QLabel(self.ModelConfigBox)
        self.activationFunctionComboBox = QtWidgets.QComboBox(self.ModelConfigBox)
        self.activationFunctionLabel = QtWidgets.QLabel(self.ModelConfigBox)
        self.optimizerLabel = QtWidgets.QLabel(self.ModelConfigBox)
        # optimizer combo box values
        self.optimizerComboBox = QtWidgets.QComboBox(self.ModelConfigBox)
        # scaling buttons set
        self.normalizationRadioButton = QtWidgets.QRadioButton(self.ModelConfigBox)
        self.standardizationRadioButton = QtWidgets.QRadioButton(self.ModelConfigBox)
        self.scalingTypeGroup = QtWidgets.QButtonGroup(self.ModelConfigBox)
        self.scalingLabel = QtWidgets.QLabel(self.ModelConfigBox)
        self.trainingLabel = QtWidgets.QLabel(self.ModelConfigBox)

        self.maximumEpochsSpinBox=10000
        self.minimumEpochsSpinBox=1000
        self.defaultSpinBoxValue=5000

        self.setupModelConfigUi()

    def setupModelConfigUi(self):
        self.ModelConfigBox.setGeometry(QtCore.QRect(10, 210, 561, 341))
        self.ModelConfigBox.setTitle("Model Config")
        self.ModelConfigBox.setDisabled(True)

        # training label
        self.trainingLabel.setGeometry(QtCore.QRect(258, 270, 271, 23))
        self.trainingLabel.setText('Training...')
        self.trainingLabel.setHidden(True)

        # train button
        self.trainButton.setGeometry(QtCore.QRect(240, 300, 101, 28))
        self.trainButton.setText("Train")

        #setting epoch spinner box values
        self.epochsSpinBox.setGeometry(QtCore.QRect(170, 40, 91, 31))        
        self.epochsSpinBox.setMaximum(self.maximumEpochsSpinBox)
        self.epochsSpinBox.setMinimum(self.minimumEpochsSpinBox)
        self.epochsSpinBox.setValue(self.defaultSpinBoxValue)


        self.EpochsLabel.setGeometry(QtCore.QRect(30, 40, 51, 31))
        self.EpochsLabel.setText("Epochs")

        self.activationFunctionComboBox.setGeometry(QtCore.QRect(170, 150, 231, 31))

        self.activationFunctionLabel.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.activationFunctionLabel.setText("Activation Function")
        self.activationFunctionComboBox.addItems(['Sigmoid','Relu','Softmax','Softplus','Softsign','Tanh','Selu','Elu','Exponential'])

        # optimizer set components
        self.optimizerLabel.setGeometry(QtCore.QRect(30, 100, 61, 31))
        self.optimizerLabel.setText("Optimizer")
        self.optimizerComboBox.setGeometry(QtCore.QRect(170, 100, 231, 31))
        self.optimizerComboBox.addItems(['Adam','SGD','RMSprop','Adadelta','Adagrad','Adamax','Nadam','Ftrl'])

        # scaling buttons
        self.normalizationRadioButton.setGeometry(QtCore.QRect(170, 210, 111, 21))
        self.normalizationRadioButton.setChecked(True)
        self.normalizationRadioButton.setText("Normalization")

        self.standardizationRadioButton.setText("Standardization")
        self.standardizationRadioButton.setGeometry(QtCore.QRect(290, 210, 121, 21))
        self.standardizationRadioButton.setChecked(False)

        # Adding all scaling buttons to a group
        self.scalingTypeGroup.addButton(self.normalizationRadioButton)
        self.scalingTypeGroup.addButton(self.standardizationRadioButton)

        self.scalingLabel.setGeometry(QtCore.QRect(30, 210, 61, 21))
        self.scalingLabel.setObjectName("scalingLabel")
        self.scalingLabel.setText("Scaling")
