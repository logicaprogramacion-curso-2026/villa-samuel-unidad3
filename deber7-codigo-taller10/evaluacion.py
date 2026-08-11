from ia import Ollama


class EvaluacionDocente:

    def __init__(self, nombre, materia, descripcion):

        self.nombre = nombre
        self.materia = materia
        self.descripcion = descripcion

        self.ia = Ollama()

    def analizar(self):

        resultados = self.ia.analizar(
            self.nombre,
            self.materia,
            self.descripcion
        )

        if resultados is None:
            return None

        return self.validar_resultados(resultados)

    def validar_resultados(self, resultados):

        criterios = [
            "recursos_digitales",
            "evaluacion",
            "empoderamiento"
        ]

        for criterio in criterios:

            if criterio not in resultados:
                print(
                    f"ERROR: Falta el criterio {criterio}"
                )
                return None

            datos = resultados[criterio]

            if "nivel" not in datos:
                return None

            if "justificacion" not in datos:
                return None

            if "sugerencia" not in datos:
                return None

            # Validar nivel
            try:
                nivel = int(datos["nivel"])

                if nivel not in [1, 2, 3]:
                    print(
                        f"ERROR: Nivel inválido en {criterio}"
                    )
                    return None

                datos["nivel"] = nivel

            except ValueError:
                return None

        return resultados