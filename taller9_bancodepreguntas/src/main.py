from database import Database
from dao import preguntaDAO
from entidad import pregunta


# Crear conexión
db = Database()

print("Conexión exitosa")


# Crear DAO
dao = preguntaDAO(db)


# Crear tabla
dao.crear_tabla()

print("Tabla preguntas creada")


# Insertar pregunta de prueba

p1 = pregunta(
    pregunta="¿Cuál es la capital de Ecuador?",
    opcion_a="Quito",
    opcion_b="Guayaquil",
    opcion_c="Cuenca",
    opcion_d="Loja",
    respuesta_correcta="A",
    dificultad="Fácil",
    tema="Geografía"
)

print("Respuesta correcta:", p1.respuesta_correcta)
dao.insertar(p1)

print("Inserción realizada")


# Mostrar todas

preguntas = dao.obtener_todas()

for p in preguntas:
    print(p)


# Buscar por ID

resultado = dao.obtener_por_id(1)

print("Pregunta encontrada:")
print(resultado)


db.cerrar()