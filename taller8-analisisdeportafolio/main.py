from foro import foro
from database import database
from foro_dao import foro_dao

database_pe = database()
foro_dao = foro_dao(database_pe)
foro_dao.crear_tabla()
foro_1 = foro(1, "el inicio del proyecto", "este proyecto nos va a causar mucho estres, pero al final va a ser util", "21/07/26", "21/07/26", "21/07/26", "Activo", "El proyecto", 1, 1, 1, 1)
foro_dao.insertar(foro_1)
database_pe.cerrar