import sys
from PyQt5.QtWidgets import *
from PyQt5. QtGui import QPixmap
from PyQt5 import QtCore

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def boton_verduras(self):
        number = "papa"
        print(number)
       
if __name__=="__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())