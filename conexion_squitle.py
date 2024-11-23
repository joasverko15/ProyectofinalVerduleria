import sqlite3

class Comunicacion:
    def __init__(self):
        self.conexion = sqlite3.connect('base_srock.db')

    def inserta_producto(self, codigo, nombre, precio, cantidad):
        cursor = self.conexion.cursor()
        bd = """INSERT INTO tabla_stock (CODIGO, NOMBRE, PRECIO, CANTIDAD)
                VALUES (?, ?, ?, ?)"""
        cursor.execute(bd, (codigo, nombre, precio, cantidad))
        self.conexion.commit()
        cursor.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM tabla_stock"
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    def busca_producto(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM tabla_stock WHERE NOMBRE = ?"
        cursor.execute(bd, (nombre_producto,))
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX

    def elimina_productos(self, nombre):
        cursor = self.conexion.cursor()
        bd = "DELETE FROM tabla_stock WHERE NOMBRE = ?"
        cursor.execute(bd, (nombre,))
        self.conexion.commit()
        cursor.close()

    def actualiza_productos(self, Id, codigo, nombre, precio, cantidad):
        cursor = self.conexion.cursor()
        bd = """UPDATE tabla_stock 
                SET CODIGO = ?, NOMBRE = ?, PRECIO = ?, CANTIDAD = ?
                WHERE ID = ?"""
        cursor.execute(bd, (codigo, nombre, precio, cantidad, Id))
        filas_afectadas = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return filas_afectadas
