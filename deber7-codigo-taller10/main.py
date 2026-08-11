from evaluacion import EvaluacionDocente
from reporte import mostrar_reporte


def main():

    print("=" * 60)
    print("       SISTEMA DE EVALUACIÓN DOCENTE CON IA")
    print("=" * 60)

    nombre = input("\nIngrese el nombre del docente: ").strip()

    materia = input("Ingrese la materia: ").strip()

    descripcion = input(
        "Describa la actividad o evaluación realizada por el docente:\n> "
    ).strip()

    # Validación
    if not nombre or not materia or not descripcion:
        print("\nERROR: Todos los campos son obligatorios.")
        return

    print("\n" + "=" * 60)
    print("Analizando la actividad mediante Ollama...")
    print("=" * 60)

    sistema = EvaluacionDocente(
        nombre,
        materia,
        descripcion
    )

    resultados = sistema.analizar()

    if resultados is None:
        print("\nNo fue posible obtener la evaluación.")
        return

    mostrar_reporte(
        nombre,
        materia,
        descripcion,
        resultados
    )


if __name__ == "__main__":
    main()