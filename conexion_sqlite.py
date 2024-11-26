import sqlite3

class Comunicacion:
    def _init_(self):
        # Crear o conectar a la base de datos
        self.conexion = sqlite3.connect("base_datos.db")
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Crear tabla de productos si no existe
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                codigo TEXT NOT NULL UNIQUE,
                cantidad INTEGER NOT NULL,
                categoria TEXT NOT NULL
            )
        """)
        # Crear tabla de carrito si es necesaria
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS carrito (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                categoria TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def inserta_producto(self, nombre, cantidad, categoria, codigo):
        try:
            self.cursor.execute("""
                INSERT INTO productos (nombre, cantidad, categoria, codigo) 
                VALUES (?, ?, ?, ?)
            """, (nombre, cantidad, categoria, codigo))
            self.conexion.commit()
        except sqlite3.IntegrityError:
            print(f"El producto con código '{codigo}' ya existe.")

    def elimina_producto(self, codigo):
        self.cursor.execute("""
            SELECT cantidad FROM productos WHERE codigo = ?
        """, (codigo,))
        producto = self.cursor.fetchone()
        if producto:
            self.cursor.execute("""
                DELETE FROM productos WHERE codigo = ?
            """, (codigo,))
            self.conexion.commit()
            return True
        return False

    def mostrar_productos(self):
        self.cursor.execute("""
            SELECT id, nombre, cantidad, categoria, codigo FROM productos
        """)
        return self.cursor.fetchall()

    def restar_stock(self, codigo, cantidad):
        self.cursor.execute("""
            SELECT cantidad FROM productos WHERE codigo = ?
        """, (codigo,))
        producto = self.cursor.fetchone()
        if producto and producto[0] >= cantidad:
            self.cursor.execute("""
                UPDATE productos SET cantidad = cantidad - ? WHERE codigo = ?
            """, (cantidad, codigo))
            self.conexion.commit()
            return True
        return False

    def sumar_stock(self, codigo, cantidad):
        self.cursor.execute("""
            UPDATE productos SET cantidad = cantidad + ? WHERE codigo = ?
        """, (cantidad, codigo))
        self.conexion.commit()

    def agregar_al_carrito(self, codigo, cantidad):
        self.cursor.execute("""
            SELECT nombre, categoria FROM productos WHERE codigo = ?
        """, (codigo,))
        producto = self.cursor.fetchone()
        if producto:
            nombre, categoria = producto
            self.cursor.execute("""
                INSERT INTO carrito (nombre, cantidad, categoria)
                VALUES (?, ?, ?)
            """, (nombre, cantidad, categoria))
            self.conexion.commit()

    def eliminar_del_carrito(self, codigo, cantidad):
        self.cursor.execute("""
            SELECT id FROM carrito WHERE codigo = ?
        """, (codigo,))
        producto = self.cursor.fetchone()
        if producto:
            self.cursor.execute("""
                DELETE FROM carrito WHERE codigo = ?
            """, (codigo,))
            self.conexion.commit()
            return True
        return False

    def obtener_stock(self, codigo):
        self.cursor.execute("""
            SELECT cantidad FROM productos WHERE codigo = ?
        """, (codigo,))
        producto = self.cursor.fetchone()
        return producto[0] if producto else 0

    def cerrar_conexion(self):
        self.conexion.close()