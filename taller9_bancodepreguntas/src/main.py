from database import Database
from dao import preguntaDAO
from gestor import Gestor
import os

# Conexión
db = Database()

print("Conexión exitosa")


# DAO
dao = preguntaDAO(db)


# Crear tabla
dao.crear_tabla()

print("Tabla preguntas creada")


# Gestor de archivos
gestor = Gestor()


print("""
========================
 CARGAR PREGUNTAS
========================

1. Cargar TXT
2. Cargar CSV
3. Cargar JSON
""")


opcion = input("Seleccione una opción: ")


if opcion == "1":
    ruta_txt = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "datos",
        "PREGUNTAS_PYTHON.txt"
    )
    gestor.cargar_desde_txt(ruta_txt)

elif opcion == "2":
    ruta_csv = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "datos",
        "PREGUNTAS_PYTHON.csv"
    )
    gestor.cargar_desde_csv(ruta_csv)

elif opcion == "3":
    ruta_json = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "datos",
        "PREGUNTAS_PYTHON.json"
    )
    gestor.cargar_desde_json(ruta_json)

else:
    print("Opción inválida")


# Guardar preguntas en SQLite

for p in gestor.preguntas:
    dao.insertar(p)


print(
    "Total preguntas guardadas:",
    len(gestor.preguntas)
)


# Mostrar algunas preguntas

for p in gestor.preguntas[:50]:
    print(p.pregunta)


db.cerrar()