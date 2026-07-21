from foro import foro
class foro_dao:
    def __init__(self, db):
        self.db = db
        
    def crear_tabla(self):
        self.db.cursor.execute('''
            CREATE TABLE IF NOT EXISTS foro (
                id_foro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo VARCHAR(150) NOT NULL,
                descripcion TEXT,
                fecha_creacion DATETIME NOT NULL,
                fecha_inicio DATETIME,
                fecha_cierre DATETIME,
                estado TEXT NOT NULL CHECK (estado IN ('Activo', 'Cerrado', 'Archivado')),
                tema_principal VARCHAR(200),
                cantidad_mensajes INTEGER DEFAULT 0,
                cantidad_participantes INTEGER DEFAULT 0,
                id_curso INTEGER NOT NULL,
                id_docente INTEGER NOT NULL
            )
        ''')
    
    def insertar(self, foro):
        self.db.cursor.execute('''
            INSERT INTO foro (titulo, descripcion, fecha_creacion, fecha_inicio, fecha_cierre, estado, tema_principal, cantidad_mensajes, cantidad_participantes, id_curso, id_docente)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
            ''', (foro.titulo, foro.descripcion, foro.fecha_creacion, foro.fecha_inicio, foro.fecha_cierre, foro.estado, foro.tema_principal, foro.cantidad_mensajes, foro.cantidad_participantes, foro.id_curso, foro.id_docente))
        self.db.conn.commit()
        return self.db.cursor.lastrowid