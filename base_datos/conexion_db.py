import sqlite3

class ConexionDB():
    def __init__(self,nombre_db):
        self.nombre_base_datos = nombre_db
        self.conn       = sqlite3.connect(f'base_datos/base_datos_db/{self.nombre_base_datos}.db')
        self.cursor     = self.conn.cursor()
    
    def cerrar_conexion(self):
        self.conn.commit()
        self.conn.close()




