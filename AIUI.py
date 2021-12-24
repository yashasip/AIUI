from PyQt5 import QtCore, QtGui, QtWidgets

from ui.MainWindow import MainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    ui = MainWindow()
    ui.setupUi()
    ui.mainWindow.show()  # Display Window

    sys.exit(app.exec_())