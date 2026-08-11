from datetime import datetime


def mostrar_reporte(
    nombre,
    materia,
    descripcion,
    resultados
):

    print("\n")
    print("=" * 70)
    print("                 INFORME DE EVALUACIÓN")
    print("=" * 70)

    print(f"\nDocente: {nombre}")
    print(f"Materia: {materia}")
    print(f"Descripción: {descripcion}")

    print("\n" + "-" * 70)
    print("1. RECURSOS DIGITALES")
    print("-" * 70)

    recursos = resultados["recursos_digitales"]

    mostrar_criterio(recursos)

    print("\n" + "-" * 70)
    print("2. EVALUACIÓN")
    print("-" * 70)

    evaluacion = resultados["evaluacion"]

    mostrar_criterio(evaluacion)

    print("\n" + "-" * 70)
    print("3. EMPODERAMIENTO DEL ESTUDIANTE")
    print("-" * 70)

    empoderamiento = resultados["empoderamiento"]

    mostrar_criterio(empoderamiento)

    print("\n" + "=" * 70)
    print("                    FIN DEL INFORME")
    print("=" * 70)


def mostrar_criterio(datos):

    nivel = datos["nivel"]

    if nivel == 1:
        descripcion_nivel = "Bajo / Necesita mejorar"

    elif nivel == 2:
        descripcion_nivel = "Medio / Aceptable"

    else:
        descripcion_nivel = "Alto / Excelente"

    print(f"\nNivel: {nivel}/3")
    print(f"Valoración: {descripcion_nivel}")

    print("\nJustificación:")
    print(datos["justificacion"])

    print("\nSugerencia:")
    print(datos["sugerencia"])