from ia import Ollama


class EvaluacionDocente:

    def __init__(
        self,
        nombre,
        materia,
        actividades
    ):

        self.nombre = nombre
        self.materia = materia
        self.actividades = actividades

        self.ia = Ollama()

    def analizar(self):

        resultados = self.ia.analizar(
            self.nombre,
            self.materia,
            self.actividades
        )

        if resultados is None:
            return None

        return self.validar_resultados(
            resultados
        )

    def validar_resultados(
        self,
        resultados
    ):

        campos_principales = [
            "resumen_general",
            "recursos_digitales",
            "evaluacion",
            "empoderamiento",
            "valoracion_global"
        ]

        for campo in campos_principales:

            if campo not in resultados:

                print(
                    f"ERROR: Falta el campo '{campo}'."
                )

                return None

        # ======================================
        # VALIDAR RESUMEN
        # ======================================

        resumen = resultados[
            "resumen_general"
        ]

        campos_resumen = [
            "cantidad_actividades",
            "analisis",
            "opinion_ia",
            "fortalezas",
            "problemas_detectados",
            "aspectos_mejorar"
        ]

        for campo in campos_resumen:

            if campo not in resumen:

                print(
                    f"ERROR: Falta '{campo}' "
                    "en resumen_general."
                )

                return None

        # ======================================
        # VALIDAR CRITERIOS
        # ======================================

        criterios = [
            "recursos_digitales",
            "evaluacion",
            "empoderamiento"
        ]

        campos_criterio = [
            "nivel",
            "justificacion",
            "opinion",
            "evidencia",
            "sugerencia"
        ]

        for criterio in criterios:

            datos = resultados[
                criterio
            ]

            for campo in campos_criterio:

                if campo not in datos:

                    print(
                        f"ERROR: Falta '{campo}' "
                        f"en {criterio}."
                    )

                    return None

            # ==================================
            # NIVEL
            # ==================================

            try:

                nivel = int(
                    datos["nivel"]
                )

            except (
                ValueError,
                TypeError
            ):

                print(
                    f"ERROR: Nivel inválido "
                    f"en {criterio}."
                )

                return None

            if nivel not in [1, 2, 3]:

                print(
                    f"ERROR: Nivel inválido "
                    f"en {criterio}."
                )

                return None

            datos["nivel"] = nivel

        # ======================================
        # VALORACIÓN GLOBAL
        # ======================================

        global_resultado = resultados[
            "valoracion_global"
        ]

        campos_globales = [
            "nivel",
            "opinion",
            "justificacion",
            "sugerencia"
        ]

        for campo in campos_globales:

            if campo not in global_resultado:

                print(
                    f"ERROR: Falta '{campo}' "
                    "en valoracion_global."
                )

                return None

        try:

            nivel_global = int(
                global_resultado["nivel"]
            )

        except (
            ValueError,
            TypeError
        ):

            print(
                "ERROR: Nivel global inválido."
            )

            return None

        if nivel_global not in [1, 2, 3]:

            print(
                "ERROR: Nivel global inválido."
            )

            return None

        global_resultado[
            "nivel"
        ] = nivel_global

        # ======================================
        # EVITAR CAMPOS VACÍOS
        # ======================================

        for criterio in criterios:

            datos = resultados[
                criterio
            ]

            for campo in [
                "justificacion",
                "opinion",
                "evidencia",
                "sugerencia"
            ]:

                if not str(
                    datos[campo]
                ).strip():

                    datos[campo] = (
                        "NO SE PROPORCIONÓ "
                        "INFORMACIÓN SUFICIENTE."
                    )

        if not str(
            resumen["opinion_ia"]
        ).strip():

            resumen[
                "opinion_ia"
            ] = (
                "La información proporcionada "
                "es insuficiente para emitir "
                "una opinión pedagógica detallada."
            )

        return resultados