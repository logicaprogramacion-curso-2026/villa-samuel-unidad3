from evaluacion import EvaluacionDocente
from reporte import mostrar_reporte, guardar_reporte


def solicitar_texto(mensaje):
    """
    Solicita un texto al usuario y evita que quede vacío.
    """

    while True:

        texto = input(mensaje).strip()

        if texto:
            return texto

        print("ERROR: Este campo no puede estar vacío.")


def solicitar_cantidad():
    """
    Solicita la cantidad de actividades.
    """

    while True:

        try:

            cantidad = int(
                input("\n¿Cuántas actividades desea registrar?: ")
            )

            if cantidad <= 0:
                print("Ingrese un número mayor que cero.")
                continue

            return cantidad

        except ValueError:

            print("ERROR: Ingrese un número entero válido.")


def main():

    print("=" * 70)
    print("           SISTEMA DE EVALUACIÓN DOCENTE CON IA")
    print("=" * 70)

    # ==========================================
    # DATOS DEL DOCENTE
    # ==========================================

    nombre = solicitar_texto(
        "\nNombre del docente: "
    )

    materia = solicitar_texto(
        "Materia: "
    )

    # ==========================================
    # CANTIDAD DE ACTIVIDADES
    # ==========================================

    cantidad = solicitar_cantidad()

    actividades = []

    print("\n" + "=" * 70)
    print("REGISTRO DE ACTIVIDADES")
    print("=" * 70)

    # ==========================================
    # REGISTRAR ACTIVIDADES
    # ==========================================

    for i in range(cantidad):

        print(f"\nACTIVIDAD {i + 1}")

        print("-" * 70)

        actividad = solicitar_texto(
            "Describa la actividad y cómo fue utilizada:\n> "
        )

        actividades.append(actividad)

    # ==========================================
    # ANÁLISIS
    # ==========================================

    print("\n" + "=" * 70)
    print("ANÁLISIS CON INTELIGENCIA ARTIFICIAL")
    print("=" * 70)

    print("\nEnviando las actividades a Ollama...")
    print("Este proceso puede tardar algunos segundos.\n")

    sistema = EvaluacionDocente(
        nombre,
        materia,
        actividades
    )

    resultados = sistema.analizar()

    # ==========================================
    # VALIDAR RESULTADO
    # ==========================================

    if resultados is None:

        print("\n" + "=" * 70)
        print("NO SE PUDO GENERAR LA EVALUACIÓN")
        print("=" * 70)

        print("""
Posibles causas:

1. Ollama no está ejecutándose.
2. El modelo no está instalado.
3. El servidor de Ollama no responde.
4. La IA devolvió una respuesta incorrecta.
""")

        return

    # ==========================================
    # MOSTRAR INFORME
    # ==========================================

    mostrar_reporte(
        nombre,
        materia,
        actividades,
        resultados
    )

    # ==========================================
    # GUARDAR INFORME
    # ==========================================

    guardar_reporte(
        nombre,
        materia,
        actividades,
        resultados
    )


if __name__ == "__main__":
    main()