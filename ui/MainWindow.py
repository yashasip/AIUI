from PyQt5 import QtCore, QtGui, QtWidgets

from ui.BinaryClassifierTab import BinaryClassifierTab
from ui.ImageRecognizerTab import ImageRecognizerTab
from ui.TextGeneratorTab import TextGeneratorTab


class MainWindow(object):
    def __init__(self) -> None:
        self.mainWindow = QtWidgets.QMainWindow()  # Main Window Creation
        self.tabs = list()

        self.setupUi()

    def setupUi(self):
        self.mainWindow.resize(1257, 760)
        self.mainWindow.setWindowTitle("AIUI")

        self.centralwidget = QtWidgets.QWidget(self.mainWindow)

        self.verticalLayoutWidget = QtWidgets.QWidget(
            self.centralwidget
        )  # Outermost Layout
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1238, 710))

        self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.tabBar = QtWidgets.QTabWidget(self.verticalLayoutWidget)

        self.tabs.append(BinaryClassifierTab())  # first tab

        # Tab Set
        self.tabBar.addTab(self.tabs[0].tab, "Binary Classifier")

        self.tabs.append(ImageRecognizerTab())  # second tab

        self.tabBar.addTab(self.tabs[1].tab, "Image Recognition")

        self.mainLayout.addWidget(self.tabBar)

        self.tabs.append(TextGeneratorTab())  # third tab
        self.tabBar.addTab(self.tabs[2].tab, "Text Generator")

        self.statusbar = QtWidgets.QStatusBar(self.mainWindow)
        self.mainWindow.setStatusBar(self.statusbar)

        self.tabBar.setCurrentIndex(0)
        # Add to central widget
        self.mainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

        #Disabling maximise button
        self.mainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        windowIcon = QtGui.QIcon('icon\\aiui-icon.png')
        self.mainWindow.setWindowIcon(windowIcon)
