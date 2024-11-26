# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_superior.setStyleSheet("Qframe{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
        self.bt_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.bt_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/almacenamiento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(130, 130))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout.addWidget(self.bt_menu)
        spacerItem = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_minimizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_minimizar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/minimizar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QtCore.QSize(66, 66))
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout.addWidget(self.bt_minimizar)
        self.bt_maximizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_maximizar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_maximizar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagenes/maximixar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_maximizar.setIcon(icon2)
        self.bt_maximizar.setIconSize(QtCore.QSize(66, 66))
        self.bt_maximizar.setObjectName("bt_maximizar")
        self.horizontalLayout.addWidget(self.bt_maximizar)
        self.bt_cerrar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_cerrar.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagenes/equis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon3)
        self.bt_cerrar.setIconSize(QtCore.QSize(100, 100))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout.addWidget(self.bt_cerrar)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contendio = QtWidgets.QFrame(self.frame)
        self.frame_contendio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contendio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contendio.setObjectName("frame_contendio")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_contendio)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_control = QtWidgets.QFrame(self.frame_contendio)
        self.frame_control.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_control.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_control.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 206, 151);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton: hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_stock = QtWidgets.QPushButton(self.frame_control)
        self.bt_stock.setMinimumSize(QtCore.QSize(0, 40))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("libro del stock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_stock.setIcon(icon4)
        self.bt_stock.setIconSize(QtCore.QSize(60, 60))
        self.bt_stock.setObjectName("bt_stock")
        self.verticalLayout_3.addWidget(self.bt_stock)
        self.bt_verduras = QtWidgets.QPushButton(self.frame_control)
        self.bt_verduras.setMinimumSize(QtCore.QSize(0, 40))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icono para verduras y frutas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_verduras.setIcon(icon5)
        self.bt_verduras.setIconSize(QtCore.QSize(60, 60))
        self.bt_verduras.setObjectName("bt_verduras")
        self.verticalLayout_3.addWidget(self.bt_verduras)
        self.bt_frutas = QtWidgets.QPushButton(self.frame_control)
        self.bt_frutas.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_frutas.setIcon(icon5)
        self.bt_frutas.setIconSize(QtCore.QSize(60, 60))
        self.bt_frutas.setObjectName("bt_frutas")
        self.verticalLayout_3.addWidget(self.bt_frutas)
        self.bt_eliminar = QtWidgets.QPushButton(self.frame_control)
        self.bt_eliminar.setMinimumSize(QtCore.QSize(0, 40))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_eliminar.setIcon(icon6)
        self.bt_eliminar.setIconSize(QtCore.QSize(60, 60))
        self.bt_eliminar.setObjectName("bt_eliminar")
        self.verticalLayout_3.addWidget(self.bt_eliminar)
        self.bt_comprar = QtWidgets.QPushButton(self.frame_control)
        self.bt_comprar.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_comprar.setIcon(icon4)
        self.bt_comprar.setIconSize(QtCore.QSize(60, 60))
        self.bt_comprar.setObjectName("bt_comprar")
        self.verticalLayout_3.addWidget(self.bt_comprar)
        self.horizontalLayout_2.addWidget(self.frame_control)
        self.frame_paginas = QtWidgets.QFrame(self.frame_contendio)
        self.frame_paginas.setStyleSheet("QFrame{\n"
"background-color: rgb(61, 61, 61)\n"
"}\n"
"\n"
"QLabel{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color: #000000ff;\n"
"color: rgb (0, 206, 151);\n"
"border: 0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"border-borrom: 2px solid rgb(61, 61, 61);\n"
"font 75 12pt \"Times New Roman\"\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover{ \n"
"background-color: rgb(0, 206, 151); \n"
"border-radius: 15px; \n"
"color: rgb(0, 0, 0); \n"
"font: 77 10pt \"Arial Black\";  \n"
"}\n"
"\n"
"QTableWidget {\n"
"background-color: rgb(255, 255, 255); \n"
"color: rgb(0, 0, 0); \n"
"gridline-color: rgb(0, 206, 151); font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"QHeaderView::section {\n"
"background-color: rgb(0, 206, 151);\n"
"border: 1px solid rgb(0, 0, 0); \n"
"font-size: 12pt; \n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"background-color: rgb(0, 0, 0); \n"
"border: 1px solid rgb(0, 206, 151);\n"
"}\n"
"\n"
"\n"
"")
        self.frame_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paginas.setObjectName("frame_paginas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_stock = QtWidgets.QWidget()
        self.page_stock.setObjectName("page_stock")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_stock)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.page_stock)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tabla_productos = QtWidgets.QTableWidget(self.page_stock)
        self.tabla_productos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabla_productos.setObjectName("tabla_productos")
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(3, item)
        self.verticalLayout_5.addWidget(self.tabla_productos)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bt_actualizar = QtWidgets.QPushButton(self.page_stock)
        self.bt_actualizar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_actualizar.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.horizontalLayout_3.addWidget(self.bt_actualizar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_stock)
        self.page_verduras = QtWidgets.QWidget()
        self.page_verduras.setObjectName("page_verduras")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_verduras)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pr_verduras = QtWidgets.QLabel(self.page_verduras)
        self.pr_verduras.setMinimumSize(QtCore.QSize(50, 50))
        self.pr_verduras.setStyleSheet("border-color: rgb(0, 170, 255);\n"
"alternate-background-color: rgb(0, 85, 0);")
        self.pr_verduras.setAlignment(QtCore.Qt.AlignCenter)
        self.pr_verduras.setObjectName("pr_verduras")
        self.verticalLayout_8.addWidget(self.pr_verduras)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 1)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lb_nombre_verduras = QtWidgets.QLabel(self.page_verduras)
        self.lb_nombre_verduras.setObjectName("lb_nombre_verduras")
        self.verticalLayout_6.addWidget(self.lb_nombre_verduras)
        self.lb_codigo_verduras = QtWidgets.QLabel(self.page_verduras)
        self.lb_codigo_verduras.setMinimumSize(QtCore.QSize(0, 1))
        self.lb_codigo_verduras.setObjectName("lb_codigo_verduras")
        self.verticalLayout_6.addWidget(self.lb_codigo_verduras)
        self.lb_cantida_verduras = QtWidgets.QLabel(self.page_verduras)
        self.lb_cantida_verduras.setObjectName("lb_cantida_verduras")
        self.verticalLayout_6.addWidget(self.lb_cantida_verduras)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.agregar_nombre_verduras = QtWidgets.QLineEdit(self.page_verduras)
        self.agregar_nombre_verduras.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.agregar_nombre_verduras.setObjectName("agregar_nombre_verduras")
        self.verticalLayout_7.addWidget(self.agregar_nombre_verduras)
        self.agregar_codigo_verduras = QtWidgets.QLineEdit(self.page_verduras)
        self.agregar_codigo_verduras.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.agregar_codigo_verduras.setObjectName("agregar_codigo_verduras")
        self.verticalLayout_7.addWidget(self.agregar_codigo_verduras)
        self.agregar_cantidad_verduras = QtWidgets.QLineEdit(self.page_verduras)
        self.agregar_cantidad_verduras.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.agregar_cantidad_verduras.setObjectName("agregar_cantidad_verduras")
        self.verticalLayout_7.addWidget(self.agregar_cantidad_verduras)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.page_verduras)
        self.label_11.setMinimumSize(QtCore.QSize(200, 0))
        self.label_11.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.bt_agregar_verdura = QtWidgets.QPushButton(self.page_verduras)
        self.bt_agregar_verdura.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_agregar_verdura.setStyleSheet("alternate-background-color: rgb(0, 255, 127);\n"
"background-color: rgb(85, 255, 0);")
        self.bt_agregar_verdura.setObjectName("bt_agregar_verdura")
        self.horizontalLayout_7.addWidget(self.bt_agregar_verdura)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_verduras)
        self.page_frutas = QtWidgets.QWidget()
        self.page_frutas.setObjectName("page_frutas")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_frutas)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_2 = QtWidgets.QLabel(self.page_frutas)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_11.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 1)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lb_producto_frutas = QtWidgets.QLabel(self.page_frutas)
        self.lb_producto_frutas.setObjectName("lb_producto_frutas")
        self.verticalLayout_10.addWidget(self.lb_producto_frutas)
        self.lb_codigo_frutas = QtWidgets.QLabel(self.page_frutas)
        self.lb_codigo_frutas.setObjectName("lb_codigo_frutas")
        self.verticalLayout_10.addWidget(self.lb_codigo_frutas)
        self.lb_cantidad_frutas = QtWidgets.QLabel(self.page_frutas)
        self.lb_cantidad_frutas.setObjectName("lb_cantidad_frutas")
        self.verticalLayout_10.addWidget(self.lb_cantidad_frutas)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.agregar_nombre_frutas = QtWidgets.QLineEdit(self.page_frutas)
        self.agregar_nombre_frutas.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.agregar_nombre_frutas.setObjectName("agregar_nombre_frutas")
        self.verticalLayout_9.addWidget(self.agregar_nombre_frutas)
        self.agregar_codigo_frutas = QtWidgets.QLineEdit(self.page_frutas)
        self.agregar_codigo_frutas.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.agregar_codigo_frutas.setObjectName("agregar_codigo_frutas")
        self.verticalLayout_9.addWidget(self.agregar_codigo_frutas)
        self.agregar_cantidad_frutas = QtWidgets.QLineEdit(self.page_frutas)
        self.agregar_cantidad_frutas.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.agregar_cantidad_frutas.setObjectName("agregar_cantidad_frutas")
        self.verticalLayout_9.addWidget(self.agregar_cantidad_frutas)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.page_frutas)
        self.label_10.setMinimumSize(QtCore.QSize(200, 0))
        self.label_10.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.bt_agregar_fruta = QtWidgets.QPushButton(self.page_frutas)
        self.bt_agregar_fruta.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_agregar_fruta.setStyleSheet("alternate-background-color: rgb(85, 255, 0);\n"
"background-color: rgb(85, 255, 0);")
        self.bt_agregar_fruta.setObjectName("bt_agregar_fruta")
        self.horizontalLayout_9.addWidget(self.bt_agregar_fruta)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.stackedWidget.addWidget(self.page_frutas)
        self.page_eliminar = QtWidgets.QWidget()
        self.page_eliminar.setObjectName("page_eliminar")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_eliminar)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.page_eliminar)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_14.addWidget(self.label_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.page_eliminar)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_eliminar)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_10.addWidget(self.lineEdit_7)
        self.pushButton = QtWidgets.QPushButton(self.page_eliminar)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout_10)
        self.tableWidget = QtWidgets.QTableWidget(self.page_eliminar)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_14.addWidget(self.tableWidget)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.page_eliminar)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        self.label_14.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_eliminar)
        self.pushButton_6.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_6.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_11.addWidget(self.pushButton_6)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.stackedWidget.addWidget(self.page_eliminar)
        self.page_carrito = QtWidgets.QWidget()
        self.page_carrito.setObjectName("page_carrito")
        self.stackedWidget.addWidget(self.page_carrito)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_paginas)
        self.verticalLayout_2.addWidget(self.frame_contendio)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_stock.setText(_translate("MainWindow", "STOCK"))
        self.bt_verduras.setText(_translate("MainWindow", "VERDURAS"))
        self.bt_frutas.setText(_translate("MainWindow", "FRUTAS"))
        self.bt_eliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.bt_comprar.setText(_translate("MainWindow", "COMPRAR"))
        self.stackedWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">FRUTAS</span></p></body></html>"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PRODUCTOS</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "PRODUCTOS"))
        item = self.tabla_productos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "nombre"))
        item = self.tabla_productos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "codigo"))
        item = self.tabla_productos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "cantidad"))
        item = self.tabla_productos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "precio"))
        self.bt_actualizar.setText(_translate("MainWindow", "actualizar"))
        self.pr_verduras.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">VERDURAS</span></p></body></html>"))
        self.pr_verduras.setText(_translate("MainWindow", "VERDURAS"))
        self.lb_nombre_verduras.setText(_translate("MainWindow", "NOMBRE"))
        self.lb_codigo_verduras.setText(_translate("MainWindow", "CODIGO"))
        self.lb_cantida_verduras.setText(_translate("MainWindow", "CANTIDAD"))
        self.bt_agregar_verdura.setText(_translate("MainWindow", "AGREGAR"))
        self.lb_producto_frutas.setText(_translate("MainWindow", "NOMBRE"))
        self.lb_codigo_frutas.setText(_translate("MainWindow", "CODIGO"))
        self.lb_cantidad_frutas.setText(_translate("MainWindow", "CANTIDAD"))
        self.bt_agregar_fruta.setText(_translate("MainWindow", "AGREGAR"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#55ffff;\">ELIMINAR PRODUCTO</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic; color:#00ffff;\">NOMBRE DEL PRODUCTO</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">BUSCAR</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "BUSCAR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CODIGO"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CANTIDAD"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ELIMINAR</span></p></body></html>"))
        self.pushButton_6.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">ELIMINAR</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "ELIMINAR"))
