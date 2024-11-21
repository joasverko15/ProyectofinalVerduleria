import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QPushButton, QVBoxLayout, QTableWidget
from MainWindow import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.carrito = []

        self.ui.bt_stock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_stock))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_verduras))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_frutas))
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminar))
        self.ui.pushButton_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_carrito))

        self.setup_verduras_page()
        self.setup_carrito_page()

    def setup_verduras_page(self):
        layout = QVBoxLayout(self.ui.page_verduras)
        self.ui.input_nombre = QLineEdit(self.ui.page_verduras)
        self.ui.input_nombre.setPlaceholderText("Nombre de la verdura")
        self.ui.input_codigo = QLineEdit(self.ui.page_verduras)
        self.ui.input_codigo.setPlaceholderText("Código")
        self.ui.input_cantidad = QLineEdit(self.ui.page_verduras)
        self.ui.input_cantidad.setPlaceholderText("Cantidad")
        self.ui.bt_agregar_verdura = QPushButton("Agregar Verdura", self.ui.page_verduras)
        self.ui.bt_agregar_verdura.clicked.connect(self.agregar_verdura)

        layout.addWidget(self.ui.input_nombre)
        layout.addWidget(self.ui.input_codigo)
        layout.addWidget(self.ui.input_cantidad)
        layout.addWidget(self.ui.bt_agregar_verdura)

    def setup_carrito_page(self):
        layout = QVBoxLayout(self.ui.page_carrito)
        self.ui.table_carrito = QTableWidget(self.ui.page_carrito)
        self.ui.table_carrito.setColumnCount(3)
        self.ui.table_carrito.setHorizontalHeaderLabels(["Nombre", "Código", "Cantidad"])
        layout.addWidget(self.ui.table_carrito)

        self.ui.bt_eliminar_carrito = QPushButton("Eliminar Seleccionado", self.ui.page_carrito)
        self.ui.bt_eliminar_carrito.clicked.connect(self.eliminar_producto)
        layout.addWidget(self.ui.bt_eliminar_carrito)

    def agregar_verdura(self):
        nombre = self.ui.input_nombre.text()
        codigo = self.ui.input_codigo.text()
        cantidad = self.ui.input_cantidad.text()

        if nombre and codigo and cantidad:
            self.carrito.append((nombre, codigo, cantidad))
            self.actualizar_carrito()
            self.ui.input_nombre.clear()
            self.ui.input_codigo.clear()
            self.ui.input_cantidad.clear()

    def actualizar_carrito(self):
        self.ui.table_carrito.setRowCount(len(self.carrito))
        for row, (nombre, codigo, cantidad) in enumerate(self.carrito):
            self.ui.table_carrito.setItem(row, 0, QTableWidgetItem(nombre))
            self.ui.table_carrito.setItem(row, 1, QTableWidgetItem(codigo))
            self.ui.table_carrito.setItem(row, 2, QTableWidgetItem(cantidad))

    def eliminar_producto(self):
        current_row = self.ui.table_carrito.currentRow()
        if current_row >= 0:
            del self.carrito[current_row]
            self.actualizar_carrito()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())