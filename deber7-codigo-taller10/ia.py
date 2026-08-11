import json
import urllib.request
import urllib.error


class Ollama:

    def __init__(self, modelo="llama3.2"):
        self.modelo = modelo
        self.url = "http://localhost:11434/api/chat"

    def analizar(self, nombre, materia, descripcion):

        prompt = f"""
Eres un experto en evaluación de prácticas docentes.

Debes analizar una actividad realizada por un docente.

DATOS DEL DOCENTE:
Nombre: {nombre}

Materia:
{materia}

DESCRIPCIÓN DE LA ACTIVIDAD:
{descripcion}

Evalúa la actividad en exactamente tres criterios:

1. Recursos digitales
2. Evaluación
3. Empoderamiento del estudiante

Para cada criterio debes asignar un nivel:

Nivel 1 = Bajo / necesita mejorar
Nivel 2 = Medio / aceptable
Nivel 3 = Alto / excelente

Además, proporciona:

- nivel
- justificacion
- sugerencia

IMPORTANTE:

La respuesta debe contener únicamente JSON válido.

Utiliza exactamente esta estructura:

{{
    "recursos_digitales": {{
        "nivel": 1,
        "justificacion": "Texto de la justificación",
        "sugerencia": "Texto de la sugerencia"
    }},
    "evaluacion": {{
        "nivel": 1,
        "justificacion": "Texto de la justificación",
        "sugerencia": "Texto de la sugerencia"
    }},
    "empoderamiento": {{
        "nivel": 1,
        "justificacion": "Texto de la justificación",
        "sugerencia": "Texto de la sugerencia"
    }}
}}

No agregues explicaciones fuera del JSON.
"""

        datos = {
            "model": self.modelo,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
            "format": "json"
        }

        try:

            datos_json = json.dumps(datos).encode("utf-8")

            solicitud = urllib.request.Request(
                self.url,
                data=datos_json,
                headers={
                    "Content-Type": "application/json"
                },
                method="POST"
            )

            with urllib.request.urlopen(
                solicitud,
                timeout=120
            ) as respuesta:

                resultado = json.loads(
                    respuesta.read().decode("utf-8")
                )

            contenido = resultado["message"]["content"]

            return json.loads(contenido)

        except urllib.error.URLError:

            print("\nERROR: No se pudo conectar con Ollama.")
            print("Verifique que Ollama esté ejecutándose.")

            return None

        except json.JSONDecodeError:

            print("\nERROR: Ollama no devolvió un JSON válido.")

            return None

        except Exception as error:

            print(f"\nERROR inesperado: {error}")

            return None