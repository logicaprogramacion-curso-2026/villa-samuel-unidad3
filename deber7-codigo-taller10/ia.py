import json
import urllib.request
import urllib.error


class Ollama:

    def __init__(self, modelo="llama3.2"):

        self.modelo = modelo
        self.url = "http://localhost:11434/api/chat"

    def analizar(
        self,
        nombre,
        materia,
        actividades
    ):

        lista_actividades = ""

        for i, actividad in enumerate(
            actividades,
            start=1
        ):

            lista_actividades += (
                f"\nACTIVIDAD {i}:\n"
                f"{actividad}\n"
            )

        prompt = f"""
Eres un experto en evaluación docente,
pedagogía, innovación educativa y diseño
de experiencias de aprendizaje.

Tu trabajo NO consiste solamente en poner una nota.

Debes actuar como:

1. EVALUADOR
2. ANALISTA
3. ASESOR PEDAGÓGICO

Debes evaluar las actividades y también DAR TU OPINIÓN
PROFESIONAL sobre la práctica docente descrita.

==================================================
DATOS
==================================================

Docente:
{nombre}

Materia:
{materia}

Cantidad de actividades:
{len(actividades)}

==================================================
ACTIVIDADES
==================================================

{lista_actividades}

==================================================
REGLA FUNDAMENTAL
==================================================

NO INVENTES INFORMACIÓN.

Debes diferenciar claramente entre:

- LO QUE REALMENTE ESTÁ EN LA DESCRIPCIÓN.
- TU OPINIÓN PROFESIONAL SOBRE ESA DESCRIPCIÓN.

Si algo no aparece explícitamente,
debes decir:

"NO EVIDENCIADO EN LAS ACTIVIDADES"

Nunca debes inventar que se utilizaron:

- computadoras
- Internet
- inteligencia artificial
- videos
- presentaciones
- rúbricas
- exámenes
- retroalimentación
- autoevaluación
- coevaluación
- trabajo colaborativo
- proyectos
- investigación
- tecnología

si no aparecen en la descripción.

==================================================
IMPORTANTE: OPINIÓN PROFESIONAL
==================================================

Aunque la actividad sea insuficiente, debes expresar
una opinión profesional.

La opinión NO debe inventar hechos.

Debe analizar la situación descrita.

Por ejemplo, si el usuario escribe:

"El docente no dio clase"

puedes decir:

"La información proporcionada evidencia que no se realizó
una actividad docente durante la situación descrita.
Desde una perspectiva pedagógica, sería recomendable
planificar una actividad alternativa que permita mantener
el proceso de aprendizaje y posteriormente evaluar
el logro de los estudiantes."

Esto es una OPINIÓN, no un hecho inventado.

==================================================
CRITERIO 1: RECURSOS DIGITALES
==================================================

Analiza:

- Cantidad de actividades con tecnología.
- Frecuencia.
- Variedad.
- Herramientas.
- Finalidad.
- Uso pedagógico.
- Participación del estudiante.
- Creación.
- Investigación.
- Práctica.
- Colaboración.

No otorgues nivel alto solamente porque
aparezca una herramienta digital.

==================================================
CRITERIO 2: EVALUACIÓN
==================================================

Analiza:

- Métodos de evaluación.
- Rúbricas.
- Pruebas.
- Proyectos.
- Criterios.
- Evaluación formativa.
- Evaluación sumativa.
- Retroalimentación.
- Autoevaluación.
- Coevaluación.
- Seguimiento.
- Oportunidades de mejora.

==================================================
CRITERIO 3: EMPODERAMIENTO
==================================================

Analiza:

- Participación.
- Autonomía.
- Investigación.
- Colaboración.
- Toma de decisiones.
- Resolución de problemas.
- Creatividad.
- Pensamiento crítico.
- Proyectos.
- Responsabilidad del estudiante.

==================================================
NIVELES
==================================================

NIVEL 1:

Existe poca o ninguna evidencia.

NIVEL 2:

Existe evidencia parcial o moderada.

NIVEL 3:

Existe evidencia clara, frecuente, variada
y pedagógicamente significativa.

La cantidad de actividades NO determina
por sí sola el nivel.

==================================================
OPINIÓN
==================================================

Debes generar una opinión general del trabajo docente.

La opinión debe responder:

- ¿Qué impresión genera la práctica descrita?
- ¿Qué está funcionando?
- ¿Qué parece faltar?
- ¿Qué impacto podría tener en el aprendizaje?
- ¿Qué debería priorizar el docente?

La opinión debe ser profesional,
clara y constructiva.

NO insultes ni ataques al docente.

==================================================
FORTALEZAS
==================================================

Incluye únicamente fortalezas respaldadas
por las actividades.

Si no hay fortalezas:

"NO SE IDENTIFICARON FORTALEZAS
SUFICIENTEMENTE EVIDENCIADAS."

==================================================
PROBLEMAS DETECTADOS
==================================================

Identifica problemas o limitaciones que puedan
deducirse de la información.

Si la descripción indica que no se realizó
una actividad, puedes señalar la ausencia
de una experiencia de aprendizaje.

==================================================
SUGERENCIAS
==================================================

Las sugerencias deben ser prácticas y concretas.

No escribas solamente:

"Mejorar la enseñanza."

En su lugar:

"Planificar una actividad práctica relacionada
con el tema, establecer un objetivo de aprendizaje,
incorporar un mecanismo de evaluación y proporcionar
retroalimentación."

==================================================
RESPUESTA JSON
==================================================

Devuelve ÚNICAMENTE JSON válido.

Utiliza exactamente esta estructura:

{{
    "resumen_general": {{
        "cantidad_actividades": {len(actividades)},
        "analisis": "",
        "opinion_ia": "",
        "fortalezas": [],
        "problemas_detectados": [],
        "aspectos_mejorar": []
    }},

    "recursos_digitales": {{
        "nivel": 1,
        "justificacion": "",
        "opinion": "",
        "evidencia": "",
        "sugerencia": ""
    }},

    "evaluacion": {{
        "nivel": 1,
        "justificacion": "",
        "opinion": "",
        "evidencia": "",
        "sugerencia": ""
    }},

    "empoderamiento": {{
        "nivel": 1,
        "justificacion": "",
        "opinion": "",
        "evidencia": "",
        "sugerencia": ""
    }},

    "valoracion_global": {{
        "nivel": 1,
        "opinion": "",
        "justificacion": "",
        "sugerencia": ""
    }}
}}

REGLAS DEL JSON:

- Los niveles solamente pueden ser 1, 2 o 3.
- Ningún campo de texto puede quedar vacío.
- Si no existe evidencia, debes escribir
  "NO EVIDENCIADO EN LAS ACTIVIDADES."
- La opinión siempre debe existir.
- Las sugerencias siempre deben existir.
- No agregues texto fuera del JSON.
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

            "format": "json",

            "options": {
                "temperature": 0.2
            }
        }

        try:

            datos_json = json.dumps(
                datos
            ).encode("utf-8")

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
                timeout=180
            ) as respuesta:

                contenido_respuesta = (
                    respuesta
                    .read()
                    .decode("utf-8")
                )

            resultado = json.loads(
                contenido_respuesta
            )

            contenido = resultado[
                "message"
            ][
                "content"
            ]

            return json.loads(
                contenido
            )

        except urllib.error.URLError as error:

            print(
                "\nERROR: No se pudo conectar con Ollama."
            )

            print(
                f"Detalle: {error}"
            )

            return None

        except json.JSONDecodeError:

            print(
                "\nERROR: Ollama no devolvió JSON válido."
            )

            return None

        except Exception as error:

            print(
                f"\nERROR inesperado: {error}"
            )

            return None 