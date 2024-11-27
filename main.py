import json
import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
from MainWindow import Ui_MainWindow
from arduino import *


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


# Subclases para Fruta y Verdura
class Fruta(Producto):
    def __init__(self, nombre, cantidad, precio):
        super().__init__(nombre, cantidad, precio)


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

        # Configuración inicial
        self.inicializar_stock()
        self.configurar_tablas()
        self.configurar_conexiones()

        # Configuración de la ventana
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.ui.lineEdit_7 
    # Métodos de inicialización
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
        tablas = [self.ui.tabla_productos, self.ui.tabla_carrito]

        for tabla in tablas:
            if not isinstance(tabla, QTableWidget):
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
        self.ui.bt_agregar_verdura.clicked.connect(self.add_to_carrito1)
        self.ui.bt_agregar_fruta.clicked.connect(self.add_to_carrito2)
        self.ui.bt_eliminar.clicked.connect(self.eliminar_del_carrito)
        self.ui.bt_menu.clicked.connect(self.toggle_frame_control)
        self.ui.bt_stock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_stock))
        self.ui.bt_comprar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_carrito))
        self.ui.bt_verduras.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_verduras))
        self.ui.bt_frutas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_frutas))
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_minimizar.clicked.connect(self.minimizar_ventana)
        self.ui.bt_comprar.clicked.connect(self.procesar_compra)

    # Métodos para actualización de tablas
    def actualizar_tabla_stock(self):
        self.ui.tabla_productos.setRowCount(0)
        for row, producto in enumerate(self.stock):
            self.ui.tabla_productos.insertRow(row)
            self.ui.tabla_productos.setItem(row, 0, QTableWidgetItem(producto.nombre))
            self.ui.tabla_productos.setItem(row, 1, QTableWidgetItem(producto.codigo))
            self.ui.tabla_productos.setItem(row, 2, QTableWidgetItem(str(producto.cantidad)))
            self.ui.tabla_productos.setItem(row, 3, QTableWidgetItem(f"${producto.precio}"))
       
    def procesar_compra(self):
        if not self.carrito.obtener_productos():
            QMessageBox.warning(self, "Error", "El carrito está vacío. No hay nada para comprar.")
        

        # Guarda los productos en el archivo JSON
        self.carrito.guardar_en_json()

        # Muestra un mensaje de confirmación
        QMessageBox.information(self, "Compra realizada", "La compra se ha procesado exitosamente. ¡Gracias!")

        # Vacía el carrito
        self.carrito.productos.clear()
        self.actualizar_tabla_carrito()
        return
    def actualizar_tabla_carrito(self):
        for row, item in enumerate(self.carrito.obtener_productos()):
            self.ui.page_carrito.insertRow(row)
            self.ui.page_carrito.setItem(row, 0, QTableWidgetItem(item["nombre"]))
            self.ui.page_carrito.setItem(row, 1, QTableWidgetItem(item["codigo"]))
            self.ui.page_carrito.setItem(row, 2, QTableWidgetItem(str(item["cantidad"])))
            self.ui.page_carrito.setItem(row, 3, QTableWidgetItem(f"${item['precio_unitario']}"))

    # Métodos principales de la funcionalidad
    def add_to_carrito1(self):
        nombre = self.ui.agregar_nombre_verduras.text()
        codigo = self.ui.agregar_codigo_verduras.text()
        cantidad_text = self.ui.agregar_cantidad_verduras.text()
        
        if not nombre or not cantidad_text.isdigit() or not codigo:
            QMessageBox.warning(self, "Error", "Complete todos los campos correctamente.")
            return

        cantidad = int(cantidad_text)
        for producto in self.stock:
            if producto.nombre.lower() == nombre.lower() and producto.codigo == codigo:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    self.carrito.agregar_producto(producto, cantidad)
                    self.actualizar_tabla_stock()
                    self.carrito.guardar_en_json()
                    QMessageBox.information(self, "Éxito", f"{cantidad} unidades de {nombre} añadidas al carrito.")
                else:
                    QMessageBox.warning(self, "Error", f"No hay suficiente stock de {nombre}.")
                return
        QMessageBox.warning(self, "Error", f"El producto '{nombre}' con código '{codigo}' no existe.")

    def add_to_carrito2(self):
        nombre = self.ui.agregar_nombre_frutas.text()
        codigo = self.ui.agregar_codigo_frutas.text()
        cantidad_text = self.ui.agregar_cantidad_frutas.text()
            
        if not nombre or not cantidad_text.isdigit() or not codigo:
            QMessageBox.warning(self, "Error", "Complete todos los campos correctamente.")
            return

        cantidad = int(cantidad_text)
        for producto in self.stock:
            if producto.nombre.lower() == nombre.lower() and producto.codigo == codigo:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    self.carrito.agregar_producto(producto, cantidad)
                    self.actualizar_tabla_stock()
                    self.carrito.guardar_en_json()
                    QMessageBox.information(self, "Éxito", f"{cantidad} unidades de {nombre} añadidas al carrito.")
                else:
                    QMessageBox.warning(self, "Error", f"No hay suficiente stock de {nombre}.")
                return
        QMessageBox.warning(self, "Error", f"El producto '{nombre}' con código '{codigo}' no existe.")


    def eliminar_del_carrito(self):
         # Obtener el nombre del producto ingresado
        nombre_producto = self.input_text.text().strip()

        if not nombre_producto:
            QMessageBox.warning(self, "Error", "Por favor ingrese un nombre de producto.")
            return

        # Cargar productos desde el archivo JSON
        with open("carrito.json", 'r') as f:
            productos = json.load(f)

        # Buscar el producto en la lista
        producto_encontrado = False
        for producto in productos:
            if producto["nombre"].lower() == nombre_producto.lower():
                productos.remove(producto)
                producto_encontrado = True
                break

        if producto_encontrado:
            # Guardar los cambios en el archivo JSON
            with open("carrito.json", 'r') as f:
                json.dump(productos, f, indent=4)

            QMessageBox.information(self, "Éxito", f"El producto '{nombre_producto}' ha sido eliminado.")
        else:
            QMessageBox.warning(self, "No encontrado", f"No se encontró el producto '{nombre_producto}'.")

    # Métodos para la interfaz
    def toggle_frame_control(self):
        width = self.ui.frame_control.width()
        extender = 200 if width == 0 else 0
        self.animacion = QPropertyAnimation(self.ui.frame_control, b"minimumWidth")
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QEasingCurve.InOutQuart)
        self.animacion.start()

    def maximizar_ventana(self):
        self.showMaximized() if not self.isMaximized() else self.showNormal()

    def minimizar_ventana(self):
        self.showMinimized()


# Punto de entrada
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
