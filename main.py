import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QComboBox, QDateEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QInputDialog, QMessageBox
from PyQt5.uic import loadUi
from datetime import date


class VerduleriaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('untitled.ui', self)  # Cargar el archivo .ui creado con Qt Designer
        self.setWindowTitle('Sistema de Verdulería')

        # Inicializar tablas
        self.init_tables()

        # Conectar botones con sus funciones
        self.bt_productos_venta.clicked.connect(self.open_productos_venta)
        self.bt_consultar_precio.clicked.connect(self.consultar_precio)
        self.bt_compra_producto.clicked.connect(self.open_compra_producto)
        self.bt_datos_maestros.clicked.connect(self.open_datos_maestros)

        # Cargar productos y operaciones desde el archivo JSON
        self.load_data()

    def init_tables(self):
        """Inicializa las tablas con cabeceras y valores predeterminados"""
        # Tabla PRODUCTOS
        self.tbl_productos.setColumnCount(4)
        self.tbl_productos.setHorizontalHeaderLabels(['Denominación', 'Tipo', 'Unidad de Medida', 'Precio Unitario'])

        # Tabla COMPRA_VENTA
        self.tbl_compra_venta.setColumnCount(8)
        self.tbl_compra_venta.setHorizontalHeaderLabels([
            'Fecha de Operación', 'Tipo de Operación', 'Denominación', 'Tipo', 'Unidad de Medida', 
            'Cantidad', 'Precio Unitario', 'Precio Total'
        ])

    def load_data(self):
        """Carga los datos de productos y operaciones desde el archivo JSON"""
        try:
            with open('productos.json', 'r') as file:
                self.productos = json.load(file)
        except FileNotFoundError:
            self.productos = []

        # Cargar productos en la tabla
        for producto in self.productos:
            row_position = self.tbl_productos.rowCount()
            self.tbl_productos.insertRow(row_position)
            self.tbl_productos.setItem(row_position, 0, QTableWidgetItem(producto['denominacion']))
            self.tbl_productos.setItem(row_position, 1, QTableWidgetItem(producto['tipo']))
            self.tbl_productos.setItem(row_position, 2, QTableWidgetItem(producto['unidad_medida']))
            self.tbl_productos.setItem(row_position, 3, QTableWidgetItem(str(producto['precio_unitario'])))

    def save_data(self):
        """Guarda los datos actuales en el archivo JSON"""
        productos = []
        for row in range(self.tbl_productos.rowCount()):
            producto = {
                'denominacion': self.tbl_productos.item(row, 0).text(),
                'tipo': self.tbl_productos.item(row, 1).text(),
                'unidad_medida': self.tbl_productos.item(row, 2).text(),
                'precio_unitario': float(self.tbl_productos.item(row, 3).text())
            }
            productos.append(producto)

        with open('productos.json', 'w') as file:
            json.dump(productos, file)

    def open_productos_venta(self):
        """Abrir la ventana de productos a vender"""
        self.open_operacion_window(tipo='Venta')

    def open_compra_producto(self):
        """Abrir la ventana de compra de productos"""
        self.open_operacion_window(tipo='Compra')

    def open_operacion_window(self, tipo):
        """Función común para abrir ventana de operaciones (Compra/Venta)"""
        ventana = QWidget()
        ventana.setWindowTitle(f"{tipo} de Producto")

        layout = QFormLayout()
        denominacion_combobox = QComboBox()
        for producto in self.productos:
            denominacion_combobox.addItem(producto['denominacion'])

        fecha = QDateEdit(date.today())
        tipo_operacion = QComboBox()
        tipo_operacion.addItem(tipo)

        cantidad_input = QLineEdit()
        precio_unitario_input = QLineEdit()

        layout.addRow('Fecha de Operación', fecha)
        layout.addRow('Tipo de Operación', tipo_operacion)
        layout.addRow('Denominación', denominacion_combobox)
        layout.addRow('Cantidad', cantidad_input)
        layout.addRow('Precio Unitario', precio_unitario_input)

        # Almacenar los datos ingresados
        def almacenar_datos():
            denominacion = denominacion_combobox.currentText()
            producto = next((prod for prod in self.productos if prod['denominacion'] == denominacion), None)
            if producto:
                precio_unitario_input.setText(str(producto['precio_unitario']))
                precio_total = float(cantidad_input.text()) * producto['precio_unitario']
                # Agregar registro a COMPRA_VENTA
                row_position = self.tbl_compra_venta.rowCount()
                self.tbl_compra_venta.insertRow(row_position)
                self.tbl_compra_venta.setItem(row_position, 0, QTableWidgetItem(str(fecha.date().toString())))
                self.tbl_compra_venta.setItem(row_position, 1, QTableWidgetItem(tipo))
                self.tbl_compra_venta.setItem(row_position, 2, QTableWidgetItem(denominacion))
                self.tbl_compra_venta.setItem(row_position, 3, QTableWidgetItem(producto['tipo']))
                self.tbl_compra_venta.setItem(row_position, 4, QTableWidgetItem(producto['unidad_medida']))
                self.tbl_compra_venta.setItem(row_position, 5, QTableWidgetItem(cantidad_input.text()))
                self.tbl_compra_venta.setItem(row_position, 6, QTableWidgetItem(precio_unitario_input.text()))
                self.tbl_compra_venta.setItem(row_position, 7, QTableWidgetItem(str(precio_total)))

        btn_almacenar = QPushButton("Almacenar")
        btn_almacenar.clicked.connect(almacenar_datos)
        layout.addWidget(btn_almacenar)

        ventana.setLayout(layout)
        ventana.show()

    def consultar_precio(self):
        """Consultar precio unitario de un producto"""
        producto, ok = QInputDialog.getText(self, 'Consultar Precio', 'Nombre del Producto:')
        if ok and producto:
            producto_encontrado = next((prod for prod in self.productos if prod['denominacion'] == producto), None)
            if producto_encontrado:
                QMessageBox.information(self, 'Precio Unitario', f'El precio unitario de {producto} es: {producto_encontrado["precio_unitario"]}')
            else:
                QMessageBox.warning(self, 'Producto no encontrado', 'El producto no existe en el inventario.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VerduleriaApp()
    window.show()
    sys.exit(app.exec_())
