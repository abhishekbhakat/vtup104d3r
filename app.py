import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5 import QtGui
from vtupload import vtqt

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = vtqt.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())