from PyQt5 import QtWidgets # Pyqt class

from ui.MainWindow import MainWindow # import ui.MainWindow components

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv) # Make application
    app.setStyle('Fusion') # theme

    ui = MainWindow()
    ui.setupUi() # setupUi
    ui.mainWindow.show()  # Display Window

    sys.exit(app.exec_()) # closing window