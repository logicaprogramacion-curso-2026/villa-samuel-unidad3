ALGORITMO Sistema_Evaluacion_Docente_IA

    // ============================================================
    // SISTEMA DE EVALUACIÓN DOCENTE CON INTELIGENCIA ARTIFICIAL
    // Pseudocódigo basado en el diagrama de flujo proporcionado
    // Compatible con la estructura de PSeInt y editable en VS Code
    // ============================================================

    // ------------------------------------------------------------
    // 1. DECLARACIÓN DE VARIABLES
    // ------------------------------------------------------------
    DEFINIR nombreDocente, materia, descripcionActividad COMO CADENA
    DEFINIR datosCompletos COMO LOGICO
    DEFINIR resultados COMO CADENA

    // Recursos Digitales
    DEFINIR nivelRecursos, justificacionRecursos, sugerenciaRecursos COMO CADENA

    // Evaluación
    DEFINIR nivelEvaluacion, justificacionEvaluacion, sugerenciaEvaluacion COMO CADENA

    // Empoderamiento del Estudiante
    DEFINIR nivelEmpoderamiento, justificacionEmpoderamiento, sugerenciaEmpoderamiento COMO CADENA

    // ------------------------------------------------------------
    // 2. INICIO DEL SISTEMA
    // ------------------------------------------------------------
    ESCRIBIR "=============================================="
    ESCRIBIR "   SISTEMA DE EVALUACIÓN DOCENTE CON IA"
    ESCRIBIR "=============================================="
    ESCRIBIR "INICIO"

    // ------------------------------------------------------------
    // 3. INGRESO DE INFORMACIÓN
    // ------------------------------------------------------------
    REPETIR

        ESCRIBIR ""
        ESCRIBIR "Ingrese el nombre del docente:"
        LEER nombreDocente

        ESCRIBIR "Ingrese la materia:"
        LEER materia

        ESCRIBIR "Ingrese la descripción de la actividad o evaluación realizada por el docente:"
        LEER descripcionActividad

        // --------------------------------------------------------
        // 4. VALIDACIÓN DE LOS DATOS
        // --------------------------------------------------------
        SI nombreDocente <> "" Y materia <> "" Y descripcionActividad <> "" ENTONCES
            datosCompletos <- VERDADERO
        SINO
            datosCompletos <- FALSO
        FIN_SI

        SI datosCompletos = FALSO ENTONCES
            ESCRIBIR ""
            ESCRIBIR "POR FAVOR, COMPLETE TODOS LOS CAMPOS."
            ESCRIBIR "Debe ingresar nombre del docente, materia y descripción de la actividad."
        FIN_SI

    HASTA QUE datosCompletos = VERDADERO

    // ------------------------------------------------------------
    // 5. ENVÍO DE LA INFORMACIÓN A LA IA
    // ------------------------------------------------------------
    ESCRIBIR ""
    ESCRIBIR "Información validada correctamente."
    ESCRIBIR "Enviando información a la Inteligencia Artificial..."

    // La IA recibe:
    // - Nombre del docente
    // - Materia
    // - Descripción de la actividad o evaluación

    resultados <- ANALIZAR_CON_IA(
        nombreDocente,
        materia,
        descripcionActividad
    )

    // ------------------------------------------------------------
    // 6. ANÁLISIS DE LA ACTIVIDAD DOCENTE
    // ------------------------------------------------------------
    ESCRIBIR "La IA está analizando la actividad docente..."
    ESCRIBIR "Generando evaluaciones y resultados..."

    // ============================================================
    // 7. DIMENSIÓN 1: RECURSOS DIGITALES
    // ============================================================
    ESCRIBIR ""
    ESCRIBIR "----------------------------------------------"
    ESCRIBIR "1. RECURSOS DIGITALES"
    ESCRIBIR "----------------------------------------------"

    nivelRecursos <- OBTENER_NIVEL(resultados, "recursos_digitales")
    justificacionRecursos <- OBTENER_JUSTIFICACION(resultados, "recursos_digitales")
    sugerenciaRecursos <- OBTENER_SUGERENCIA(resultados, "recursos_digitales")

    ESCRIBIR "Nivel (1 - 2 - 3): ", nivelRecursos
    ESCRIBIR "Justificación: ", justificacionRecursos
    ESCRIBIR "Sugerencia: ", sugerenciaRecursos

    // ============================================================
    // 8. DIMENSIÓN 2: EVALUACIÓN
    // ============================================================
    ESCRIBIR ""
    ESCRIBIR "----------------------------------------------"
    ESCRIBIR "2. EVALUACIÓN"
    ESCRIBIR "----------------------------------------------"

    nivelEvaluacion <- OBTENER_NIVEL(resultados, "evaluacion")
    justificacionEvaluacion <- OBTENER_JUSTIFICACION(resultados, "evaluacion")
    sugerenciaEvaluacion <- OBTENER_SUGERENCIA(resultados, "evaluacion")

    ESCRIBIR "Nivel (1 - 2 - 3): ", nivelEvaluacion
    ESCRIBIR "Justificación: ", justificacionEvaluacion
    ESCRIBIR "Sugerencia: ", sugerenciaEvaluacion

    // ============================================================
    // 9. DIMENSIÓN 3: EMPODERAMIENTO DEL ESTUDIANTE
    // ============================================================
    ESCRIBIR ""
    ESCRIBIR "----------------------------------------------"
    ESCRIBIR "3. EMPODERAMIENTO DEL ESTUDIANTE"
    ESCRIBIR "----------------------------------------------"

    nivelEmpoderamiento <- OBTENER_NIVEL(resultados, "empoderamiento_estudiante")
    justificacionEmpoderamiento <- OBTENER_JUSTIFICACION(resultados, "empoderamiento_estudiante")
    sugerenciaEmpoderamiento <- OBTENER_SUGERENCIA(resultados, "empoderamiento_estudiante")

    ESCRIBIR "Nivel (1 - 2 - 3): ", nivelEmpoderamiento
    ESCRIBIR "Justificación: ", justificacionEmpoderamiento
    ESCRIBIR "Sugerencia: ", sugerenciaEmpoderamiento

    // ------------------------------------------------------------
    // 10. GENERAR INFORME FINAL
    // ------------------------------------------------------------
    ESCRIBIR ""
    ESCRIBIR "Generando informe final..."

    GENERAR_INFORME(
        nombreDocente,
        materia,
        descripcionActividad,
        nivelRecursos,
        justificacionRecursos,
        sugerenciaRecursos,
        nivelEvaluacion,
        justificacionEvaluacion,
        sugerenciaEvaluacion,
        nivelEmpoderamiento,
        justificacionEmpoderamiento,
        sugerenciaEmpoderamiento
    )

    // El informe final contiene:
    // - Nombre del docente
    // - Materia
    // - Descripción de la actividad
    // - Resultados de Recursos Digitales
    // - Resultados de Evaluación
    // - Resultados de Empoderamiento del Estudiante
    // Cada resultado incluye nivel, justificación y sugerencia.

    // ------------------------------------------------------------
    // 11. MOSTRAR RESULTADOS AL USUARIO
    // ------------------------------------------------------------
    ESCRIBIR ""
    ESCRIBIR "=============================================="
    ESCRIBIR "           INFORME FINAL"
    ESCRIBIR "=============================================="
    ESCRIBIR "Nombre del docente: ", nombreDocente
    ESCRIBIR "Materia: ", materia
    ESCRIBIR "Descripción de la actividad: ", descripcionActividad

    ESCRIBIR ""
    ESCRIBIR "1. RECURSOS DIGITALES"
    ESCRIBIR "Nivel: ", nivelRecursos
    ESCRIBIR "Justificación: ", justificacionRecursos
    ESCRIBIR "Sugerencia: ", sugerenciaRecursos

    ESCRIBIR ""
    ESCRIBIR "2. EVALUACIÓN"
    ESCRIBIR "Nivel: ", nivelEvaluacion
    ESCRIBIR "Justificación: ", justificacionEvaluacion
    ESCRIBIR "Sugerencia: ", sugerenciaEvaluacion

    ESCRIBIR ""
    ESCRIBIR "3. EMPODERAMIENTO DEL ESTUDIANTE"
    ESCRIBIR "Nivel: ", nivelEmpoderamiento
    ESCRIBIR "Justificación: ", justificacionEmpoderamiento
    ESCRIBIR "Sugerencia: ", sugerenciaEmpoderamiento

    ESCRIBIR ""
    ESCRIBIR "Informe generado correctamente."
    ESCRIBIR "FIN"

FIN_ALGORITMO


// ================================================================
// FUNCIONES UTILIZADAS POR EL SISTEMA
// Estas funciones representan procesos que posteriormente pueden
// implementarse en Python, JavaScript u otro lenguaje.
// ================================================================

FUNCION ANALIZAR_CON_IA(nombreDocente, materia, descripcionActividad)

    // En una implementación real:
    // 1. Construir el prompt para la IA.
    // 2. Enviar los datos a un modelo de IA.
    // 3. Solicitar una evaluación estructurada.
    // 4. Recibir y validar la respuesta.
    // 5. Devolver los resultados de las tres dimensiones.

    DEVOLVER resultadosGeneradosPorIA

FIN_FUNCION


FUNCION OBTENER_NIVEL(resultados, dimension)

    // Obtiene el nivel asignado por la IA.
    // El nivel debe corresponder a 1, 2 o 3.

    DEVOLVER nivel

FIN_FUNCION


FUNCION OBTENER_JUSTIFICACION(resultados, dimension)

    // Obtiene la explicación de por qué la actividad
    // recibió el nivel correspondiente.

    DEVOLVER justificacion

FIN_FUNCION


FUNCION OBTENER_SUGERENCIA(resultados, dimension)

    // Obtiene una recomendación de mejora generada por la IA.

    DEVOLVER sugerencia

FIN_FUNCION


PROCEDIMIENTO GENERAR_INFORME(
    nombreDocente,
    materia,
    descripcionActividad,
    nivelRecursos,
    justificacionRecursos,
    sugerenciaRecursos,
    nivelEvaluacion,
    justificacionEvaluacion,
    sugerenciaEvaluacion,
    nivelEmpoderamiento,
    justificacionEmpoderamiento,
    sugerenciaEmpoderamiento
)

    // Crear un documento con todos los datos y resultados.
    // El formato puede ser PDF, Word, HTML o TXT.

    ESCRIBIR "Documento de informe creado."

FIN_PROCEDIMIENTO
