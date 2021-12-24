from PyQt5 import QtCore, QtGui, QtWidgets

from ui.BinaryClassifierTab import BinaryClassifierTab
from ui.ImageRecognizerTab import ImageRecognizerTab
from ui.MenuBar import MenuBar


class MainWindow(object):
    def __init__(self) -> None:
        self.mainWindow = QtWidgets.QMainWindow()  # Main Window Creation
        self.tabs = list()

        self.setupUi()

    def setupUi(self):
        self.mainWindow.resize(1275, 795)
        self.mainWindow.setWindowTitle("AIUI")

        self.centralwidget = QtWidgets.QWidget(self.mainWindow)

        self.verticalLayoutWidget = QtWidgets.QWidget(
            self.centralwidget
        )  # Outermost Layout
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1261, 721))

        self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.tabBar = QtWidgets.QTabWidget(self.verticalLayoutWidget)

        self.tabs.append(BinaryClassifierTab())  # first tab

        # Tab Set
        self.tabBar.addTab(self.tabs[0].tab, "Binary Classifier")

        self.tabs.append(ImageRecognizerTab())  # first tab
        self.tabBar.setCurrentIndex(0)

        self.tabBar.addTab(self.tabs[1].tab, "Image Recognition")

        self.mainLayout.addWidget(self.tabBar)

        # Menu Bar set
        self.menuBar = MenuBar(self.mainWindow)
        self.statusbar = QtWidgets.QStatusBar(self.mainWindow)
        self.mainWindow.setStatusBar(self.statusbar)

        # Add to central widget
        self.mainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

        #Disabling maximise button
        self.mainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
