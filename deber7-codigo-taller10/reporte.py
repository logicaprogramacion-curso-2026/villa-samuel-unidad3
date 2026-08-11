import json
import os
from datetime import datetime


CARPETA_RESULTADOS = "resultados"


def obtener_valoracion(nivel):

    if nivel == 1:
        return "BAJO / NECESITA MEJORAR"

    if nivel == 2:
        return "MEDIO / ACEPTABLE"

    return "ALTO / EXCELENTE"


def mostrar_reporte(
    nombre,
    materia,
    actividades,
    resultados
):

    print("\n")

    print("=" * 75)
    print("              INFORME DE EVALUACIÓN DOCENTE")
    print("=" * 75)

    print(f"\nDocente: {nombre}")
    print(f"Materia: {materia}")

    print(
        f"Cantidad de actividades: "
        f"{len(actividades)}"
    )

    # ==========================================
    # ACTIVIDADES
    # ==========================================

    print("\n" + "-" * 75)
    print("ACTIVIDADES ANALIZADAS")
    print("-" * 75)

    for i, actividad in enumerate(
        actividades,
        start=1
    ):

        print(f"\nActividad {i}:")
        print(actividad)

    # ==========================================
    # ANÁLISIS GENERAL
    # ==========================================

    resumen = resultados[
        "resumen_general"
    ]

    print("\n" + "=" * 75)
    print("ANÁLISIS GENERAL")
    print("=" * 75)

    print(
        f"\nActividades analizadas: "
        f"{resumen['cantidad_actividades']}"
    )

    print("\nAnálisis:")

    print(
        resumen["analisis"]
    )

    # ==========================================
    # OPINIÓN DE LA IA
    # ==========================================

    print("\n" + "-" * 75)
    print("OPINIÓN PROFESIONAL DE LA IA")
    print("-" * 75)

    print(
        resumen["opinion_ia"]
    )

    # ==========================================
    # FORTALEZAS
    # ==========================================

    print("\n" + "-" * 75)
    print("FORTALEZAS")
    print("-" * 75)

    for fortaleza in resumen[
        "fortalezas"
    ]:

        print(
            f"• {fortaleza}"
        )

    # ==========================================
    # PROBLEMAS
    # ==========================================

    print("\n" + "-" * 75)
    print("PROBLEMAS DETECTADOS")
    print("-" * 75)

    for problema in resumen[
        "problemas_detectados"
    ]:

        print(
            f"• {problema}"
        )

    # ==========================================
    # ASPECTOS POR MEJORAR
    # ==========================================

    print("\n" + "-" * 75)
    print("ASPECTOS POR MEJORAR")
    print("-" * 75)

    for aspecto in resumen[
        "aspectos_mejorar"
    ]:

        print(
            f"• {aspecto}"
        )

    # ==========================================
    # CRITERIOS
    # ==========================================

    mostrar_criterio(
        "1. RECURSOS DIGITALES",
        resultados[
            "recursos_digitales"
        ]
    )

    mostrar_criterio(
        "2. EVALUACIÓN",
        resultados[
            "evaluacion"
        ]
    )

    mostrar_criterio(
        "3. EMPODERAMIENTO DEL ESTUDIANTE",
        resultados[
            "empoderamiento"
        ]
    )

    # ==========================================
    # VALORACIÓN GLOBAL
    # ==========================================

    global_resultado = resultados[
        "valoracion_global"
    ]

    print("\n" + "=" * 75)
    print("VALORACIÓN GLOBAL")
    print("=" * 75)

    nivel = global_resultado[
        "nivel"
    ]

    print(
        f"\nNivel: {nivel}/3"
    )

    print(
        f"Valoración: "
        f"{obtener_valoracion(nivel)}"
    )

    print(
        "\nOpinión general de la IA:"
    )

    print(
        global_resultado[
            "opinion"
        ]
    )

    print(
        "\nJustificación:"
    )

    print(
        global_resultado[
            "justificacion"
        ]
    )

    print(
        "\nSugerencia principal:"
    )

    print(
        global_resultado[
            "sugerencia"
        ]
    )

    print("\n" + "=" * 75)
    print("                    FIN DEL INFORME")
    print("=" * 75)


def mostrar_criterio(
    titulo,
    datos
):

    print("\n" + "=" * 75)
    print(titulo)
    print("=" * 75)

    nivel = datos[
        "nivel"
    ]

    print(
        f"\nNivel: {nivel}/3"
    )

    print(
        f"Valoración: "
        f"{obtener_valoracion(nivel)}"
    )

    print(
        "\nJustificación:"
    )

    print(
        datos[
            "justificacion"
        ]
    )

    print(
        "\nOpinión de la IA:"
    )

    print(
        datos[
            "opinion"
        ]
    )

    print(
        "\nEvidencia encontrada:"
    )

    print(
        datos[
            "evidencia"
        ]
    )

    print(
        "\nSugerencia:"
    )

    print(
        datos[
            "sugerencia"
        ]
    )


def guardar_reporte(
    nombre,
    materia,
    actividades,
    resultados
):

    os.makedirs(
        CARPETA_RESULTADOS,
        exist_ok=True
    )

    fecha = datetime.now()

    nombre_archivo = (
        "evaluacion_"
        + fecha.strftime(
            "%Y%m%d_%H%M%S"
        )
    )

    datos = {

        "fecha": fecha.isoformat(),

        "docente": nombre,

        "materia": materia,

        "actividades": actividades,

        "resultados": resultados
    }

    ruta_json = os.path.join(
        CARPETA_RESULTADOS,
        nombre_archivo + ".json"
    )

    with open(
        ruta_json,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos,
            archivo,
            ensure_ascii=False,
            indent=4
        )

    ruta_txt = os.path.join(
        CARPETA_RESULTADOS,
        nombre_archivo + ".txt"
    )

    with open(
        ruta_txt,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            generar_texto_reporte(
                nombre,
                materia,
                actividades,
                resultados
            )
        )

    print("\n")
    print("=" * 75)
    print("REPORTES GUARDADOS")
    print("=" * 75)

    print(
        f"\nJSON: {ruta_json}"
    )

    print(
        f"TXT:  {ruta_txt}"
    )


def generar_texto_reporte(
    nombre,
    materia,
    actividades,
    resultados
):

    texto = ""

    texto += (
        "INFORME DE EVALUACIÓN DOCENTE\n"
    )

    texto += "=" * 75
    texto += "\n\n"

    texto += (
        f"Docente: {nombre}\n"
    )

    texto += (
        f"Materia: {materia}\n"
    )

    texto += (
        f"Cantidad de actividades: "
        f"{len(actividades)}\n"
    )

    resumen = resultados[
        "resumen_general"
    ]

    texto += "\n\nANÁLISIS GENERAL\n"
    texto += "=" * 75
    texto += "\n"

    texto += (
        resumen["analisis"]
        + "\n"
    )

    texto += "\nOPINIÓN DE LA IA\n"

    texto += (
        resumen["opinion_ia"]
        + "\n"
    )

    texto += "\nFORTALEZAS\n"

    for fortaleza in resumen[
        "fortalezas"
    ]:

        texto += (
            f"- {fortaleza}\n"
        )

    texto += "\nPROBLEMAS DETECTADOS\n"

    for problema in resumen[
        "problemas_detectados"
    ]:

        texto += (
            f"- {problema}\n"
        )

    texto += "\nASPECTOS POR MEJORAR\n"

    for aspecto in resumen[
        "aspectos_mejorar"
    ]:

        texto += (
            f"- {aspecto}\n"
        )

    criterios = [

        (
            "RECURSOS DIGITALES",
            "recursos_digitales"
        ),

        (
            "EVALUACIÓN",
            "evaluacion"
        ),

        (
            "EMPODERAMIENTO DEL ESTUDIANTE",
            "empoderamiento"
        )
    ]

    for titulo, clave in criterios:

        datos = resultados[
            clave
        ]

        texto += "\n\n"
        texto += titulo
        texto += "\n"
        texto += "=" * 75
        texto += "\n"

        texto += (
            f"\nNivel: "
            f"{datos['nivel']}/3\n"
        )

        texto += (
            f"Valoración: "
            f"{obtener_valoracion(datos['nivel'])}\n"
        )

        texto += "\nJustificación:\n"

        texto += (
            datos["justificacion"]
            + "\n"
        )

        texto += "\nOpinión:\n"

        texto += (
            datos["opinion"]
            + "\n"
        )

        texto += "\nEvidencia:\n"

        texto += (
            datos["evidencia"]
            + "\n"
        )

        texto += "\nSugerencia:\n"

        texto += (
            datos["sugerencia"]
            + "\n"
        )

    global_resultado = resultados[
        "valoracion_global"
    ]

    texto += "\n\nVALORACIÓN GLOBAL\n"
    texto += "=" * 75
    texto += "\n"

    texto += (
        f"\nNivel: "
        f"{global_resultado['nivel']}/3\n"
    )

    texto += "\nOpinión:\n"

    texto += (
        global_resultado[
            "opinion"
        ]
        + "\n"
    )

    texto += "\nJustificación:\n"

    texto += (
        global_resultado[
            "justificacion"
        ]
        + "\n"
    )

    texto += "\nSugerencia:\n"

    texto += (
        global_resultado[
            "sugerencia"
        ]
        + "\n"
    )

    return texto