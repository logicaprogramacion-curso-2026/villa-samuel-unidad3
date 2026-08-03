import random
import json
import os


class Simulador:

    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas_usuario = []
        self.puntaje = 0
        self.total = 0


    def iniciar_simulacion(self, cantidad):

        if cantidad > len(self.preguntas):
            cantidad = len(self.preguntas)

        preguntas_seleccionadas = random.sample(
            self.preguntas, cantidad
        )

        self.total = cantidad

        print("\n===== SIMULADOR DE PREGUNTAS =====")

        for pregunta in preguntas_seleccionadas:
            self.mostrar_pregunta(pregunta)

        print("\nSimulación finalizada")
        print(f"Puntaje obtenido: {self.puntaje}/{self.total}")


    def mostrar_pregunta(self, pregunta):

        print("\n--------------------------------")
        print(pregunta.pregunta)

        print(f"A) {pregunta.opcion_a}")
        print(f"B) {pregunta.opcion_b}")
        print(f"C) {pregunta.opcion_c}")
        print(f"D) {pregunta.opcion_d}")

        respuesta = input("Seleccione una respuesta (A-D): ").upper()

        correcta = self.validar_respuesta(
            respuesta,
            pregunta.respuesta_correcta
        )

        if correcta:
            print("✓ Respuesta correcta")
            self.puntaje += 1
        else:
            print(
                f"✗ Respuesta incorrecta. "
                f"La respuesta era {pregunta.respuesta_correcta}"
            )

        self.respuestas_usuario.append(
            {
                "pregunta": pregunta.pregunta,
                "respuesta_usuario": respuesta,
                "respuesta_correcta": pregunta.respuesta_correcta,
                "resultado": correcta
            }
        )


    def validar_respuesta(self, respuesta, correcta):

        opciones_validas = ["A", "B", "C", "D"]

        if respuesta not in opciones_validas:
            return False

        return respuesta == correcta
    
    def generar_reporte(self):
    
        reporte = {
            "total_preguntas": self.total,
            "respuestas_correctas": self.puntaje,
            "respuestas_incorrectas": self.total - self.puntaje,
            "porcentaje": (
                (self.puntaje / self.total) * 100
                if self.total > 0 else 0
            ),
            "detalle": self.respuestas_usuario
        }


        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        ruta_resultados = os.path.join(
            BASE_DIR,
            "resultados"
        )


        os.makedirs(
            ruta_resultados,
            exist_ok=True
        )


        ruta = os.path.join(
            ruta_resultados,
            "reporte.json"
        )


        with open(
            ruta,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                reporte,
                archivo,
                indent=4,
                ensure_ascii=False
            )


        print("\nReporte generado correctamente")
        print(f"Archivo: {ruta}")


