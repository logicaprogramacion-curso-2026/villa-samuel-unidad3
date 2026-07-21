import sqlite3

class database:
    def __init__ (self,
                  db_name="analisisdeportafolio.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        print("conexion exitosa")
        
    def cerrar(self):
        self.conn.close()
        