from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from MainWindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Estado inicial del frame_control
        self.frame_control_expanded = False

        # Inicialización del carrito (almacena productos en una lista)
        self.carrito = []

        # Conexión de botones
        self.ui.bt_menu.clicked.connect(self.toggle_frame_control)  # Animación del menú
        self.ui.bt_stock.clicked.connect(self.show_stock_page)      # Ir a la página de stock
        self.ui.bt_verduras.clicked.connect(self.show_verduras_page)  # Ir a la página de verduras
        self.ui.bt_frutas.clicked.connect(self.show_frutas_page)      # Ir a la página de frutas
        self.ui.bt_eliminar.clicked.connect(self.show_eliminar_page)  # Ir a la página de eliminar
        self.ui.bt_carrito.clicked.connect(self.show_carrito_page)    # Ir a la página del carrito

        # Funciones para agregar al carrito
        self.ui.bt_actualizar.clicked.connect(self.add_to_carrito)

        # Maximizar, minimizar y cerrar
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_minimizar.clicked.connect(self.minimizar_ventana)
        self.ui.bt_cerrar.clicked.connect(self.close)

    # Función para mostrar/ocultar el frame_control con animación
    def toggle_frame_control(self):
        if self.frame_control_expanded:
            start_width = 200
            end_width = 0
        else:
            start_width = 0
            end_width = 200

        self.animation = QPropertyAnimation(self.ui.frame_control, b"minimumWidth")
        self.animation.setDuration(500)  # Duración en milisegundos
        self.animation.setStartValue(start_width)
        self.animation.setEndValue(end_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

        self.frame_control_expanded = not self.frame_control_expanded

    # Funciones para cambiar de página
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
        self.update_carrito_table()  # Actualizar el carrito al mostrar la página

    # Función para agregar productos al carrito
    def add_to_carrito(self):
        # Simular que se selecciona un producto (puedes adaptarlo a tus necesidades)
        producto = self.ui.label.text()  # Nombre del producto (por ejemplo, desde un label)
        cantidad = 1  # Cantidad fija por ahora (puedes agregar inputs para definir cantidad)

        self.carrito.append({"producto": producto, "cantidad": cantidad})
        print(f"Producto agregado: {producto}, Cantidad: {cantidad}")  # Debug

    # Actualizar el contenido de la tabla del carrito
    def update_carrito_table(self):
        self.ui.tableWidget.setRowCount(len(self.carrito))  # Establecer el número de filas
        self.ui.tableWidget.setColumnCount(2)  # Dos columnas: Producto y Cantidad
        self.ui.tableWidget.setHorizontalHeaderLabels(["Producto", "Cantidad"])  # Encabezados

        for row, item in enumerate(self.carrito):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(item["producto"]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(item["cantidad"])))

    # Funciones para maximizar, minimizar y cerrar ventana
    def maximizar_ventana(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def minimizar_ventana(self):
        self.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())