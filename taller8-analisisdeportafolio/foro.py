class foro:
    def __init__(self,
                 id_foro=0,
                 titulo="",
                 descripcion="",
                 fecha_creacion="",
                 fecha_inicio="",
                 fecha_cierre="",
                 estado="",
                 tema_principal="",
                 cantidad_mensajes=0,
                 cantidad_participantes=0,
                 id_curso=0,
                 id_docente=0):

        self.id_foro = id_foro
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.fecha_inicio = fecha_inicio
        self.fecha_cierre = fecha_cierre
        self.estado = estado
        self.tema_principal = tema_principal
        self.cantidad_mensajes = cantidad_mensajes
        self.cantidad_participantes = cantidad_participantes
        self.id_curso = id_curso
        self.id_docente = id_docente

        print("Constructor con argumentos")