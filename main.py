from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bt_stock.clicked.connect(self.show_stock_page)
        self.ui.pushButton_2.clicked.connect(self.show_verduras_page)
        self.ui.pushButton_3.clicked.connect(self.show_frutas_page)
        self.ui.pushButton_4.clicked.connect(self.show_eliminar_page)
        self.ui.pushButton_5.clicked.connect(self.show_carrito_page)

    def show_stock_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_stock) 

    def show_verduras_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_verduras)

    def show_frutas_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_frutas) 

    def show_eliminar_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminar) 

    def show_carrito_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_carrito)     

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
