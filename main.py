import json
import random
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox, QTableWidget
)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from MainWindow import Ui_MainWindow
import sys


# Clase base para productos
class Producto:
    def __init__(self, nombre, cantidad, precio, codigo=None):
        self.nombre = nombre.capitalize()
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo or self.generar_codigo_binario()

    @staticmethod
    def generar_codigo_binario():
        return ''.join(random.choice('01') for _ in range(6))


# Subclase Fruta
class Fruta(Producto):
    def __init__(self, nombre, cantidad, precio):
        super().__init__(nombre, cantidad, precio)


# Subclase Verdura
class Verdura(Producto):
    def __init__(self, nombre, cantidad, precio):
        super().__init__(nombre, cantidad, precio)


# Clase para administrar el carrito
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        for item in self.productos:
            if item["nombre"] == producto.nombre:
                item["cantidad"] += cantidad
                return
        self.productos.append({
            "nombre": producto.nombre,
            "cantidad": cantidad,
            "precio_unitario": producto.precio,
            "codigo": producto.codigo
        })

    def eliminar_producto(self, nombre, cantidad):
        for item in self.productos:
            if item["nombre"].lower() == nombre.lower():
                item["cantidad"] -= cantidad
                if item["cantidad"] <= 0:
                    self.productos.remove(item)
                return True
        return False

    def guardar_en_json(self, archivo="carrito.json"):
        with open(archivo, "w") as f:
            json.dump(self.productos, f, indent=4)

    def obtener_productos(self):
        return self.productos


# Clase principal para la ventana
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicializar stock y carrito
        self.stock = []
        self.carrito = Carrito()

        # Llenar el stock inicial
        self.inicializar_stock()

        # Configurar tablas
        self.configurar_tablas()

        # Conexiones de botones
        self.configurar_conexiones()

    def inicializar_stock(self):
        frutas = [
            Fruta("Manzana", 50, 10), Fruta("Pera", 30, 15), Fruta("Uva", 100, 12),
            Fruta("Naranja", 40, 8), Fruta("Frutilla", 25, 20)
        ]
        verduras = [
            Verdura("Papa", 60, 5), Verdura("Cebolla", 45, 7), Verdura("Tomate", 35, 10),
            Verdura("Zanahoria", 20, 8), Verdura("Calabaza", 15, 9)
        ]
        self.stock.extend(frutas + verduras)
        self.actualizar_tabla_stock()

    def configurar_tablas(self):
        # Asegúrate de que las tablas sean QTableWidget
        tablas = [self.ui.tabla_productos, self.ui.tabla_carrito]

        for tabla in tablas:
            if not isinstance(tabla, QTableWidget):  # Verifica que sea QTableWidget
                raise TypeError("Se espera un QTableWidget, pero se encontró un tipo diferente.")
                
            tabla.setColumnCount(4)
            tabla.setHorizontalHeaderLabels(["Producto", "Código", "Cantidad", "Precio ($)"])
            header = tabla.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
            tabla.setAlternatingRowColors(True)
            tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
            tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
            tabla.setSelectionMode(QAbstractItemView.SingleSelection)

    def configurar_conexiones(self):
        self.ui.bt_agregar_verdura.clicked.connect(self.add_to_carrito)
        self.ui.bt_eliminar.clicked.connect(self.eliminar_del_carrito)
        self.ui.bt_menu.clicked.connect(self.toggle_frame_control)
        self.ui.bt_stock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_stock))
        self.ui.bt_comprar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_carrito))
        self.ui.bt_verduras.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_verduras))
        self.ui.bt_frutas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_frutas))
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_minimizar.clicked.connect(self.minimizar_ventana)
        self.ui.bt_cerrar.clicked.connect(self.close)

    def actualizar_tabla_stock(self):
        self.ui.tabla_productos.setRowCount(0)
        for row, producto in enumerate(self.stock):
            self.ui.tabla_productos.insertRow(row)
            self.ui.tabla_productos.setItem(row, 0, QTableWidgetItem(producto.nombre))
            self.ui.tabla_productos.setItem(row, 1, QTableWidgetItem(producto.codigo))
            self.ui.tabla_productos.setItem(row, 2, QTableWidgetItem(str(producto.cantidad)))
            self.ui.tabla_productos.setItem(row, 3, QTableWidgetItem(f"${producto.precio}"))

    def actualizar_tabla_carrito(self):
        self.ui.page_carrito.setRowCount(0)  # Asegurarse de que la tabla esté vacía
        for row, item in enumerate(self.carrito.obtener_productos()):
            self.ui.page_carrito.insertRow(row)
            self.ui.page_carrito.setItem(row, 0, QTableWidgetItem(item["nombre"]))
            self.ui.page_carrito.setItem(row, 1, QTableWidgetItem(item["codigo"]))
            self.ui.page_carrito.setItem(row, 2, QTableWidgetItem(str(item["cantidad"])))
            self.ui.page_carrito.setItem(row, 3, QTableWidgetItem(f"${item['precio_unitario']}"))

    def add_to_carrito(self):
        nombre = self.ui.agregar_nombre_verduras.text()
        cantidad_text = self.ui.agregar_cantidad_verduras.text()

        if not nombre or not cantidad_text.isdigit():
            QMessageBox.warning(self, "Error", "Por favor, ingrese un nombre y una cantidad válida.")
            return

        cantidad = int(cantidad_text)
        for producto in self.stock:
            if producto.nombre.lower() == nombre.lower():
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    self.carrito.agregar_producto(producto, cantidad)
                    self.actualizar_tabla_stock()
                    self.actualizar_tabla_carrito()
                    self.carrito.guardar_en_json()
                    QMessageBox.information(self, "Éxito", f"{cantidad} unidades de {producto.nombre} añadidas al carrito.")
                else:
                    QMessageBox.warning(self, "Error", f"No hay suficiente stock de {producto.nombre}.")
                return
        QMessageBox.warning(self, "Error", f"El producto '{nombre}' no existe.")

    def eliminar_del_carrito(self):
        nombre = self.ui.eliminar_nombre.text()
        cantidad_text = self.ui.eliminar_cantidad.text()

        if not nombre or not cantidad_text.isdigit():
            QMessageBox.warning(self, "Error", "Por favor, ingrese un nombre y una cantidad válida.")
            return

        cantidad = int(cantidad_text)
        if self.carrito.eliminar_producto(nombre, cantidad):
            for producto in self.stock:
                if producto.nombre.lower() == nombre.lower():
                    producto.cantidad += cantidad
                    self.actualizar_tabla_stock()
                    self.actualizar_tabla_carrito()
                    self.carrito.guardar_en_json()
                    QMessageBox.information(self, "Éxito", f"{cantidad} unidades de {nombre} eliminadas del carrito.")
                    return
        QMessageBox.warning(self, "Error", f"No se encontró {nombre} en el carrito.")

    def toggle_frame_control(self):
    
        width = self.frame_control.width()
        normal = 0
        extender = 200 if width == 0 else normal
        self.animacion = QPropertyAnimation(self.frame_control, b"minimumWidth")
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

    def maximizar_ventana(self):
        self.showMaximized() if not self.isMaximized() else self.showNormal()

    def minimizar_ventana(self):
        self.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
