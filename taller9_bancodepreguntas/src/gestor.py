import pandas as pd
from entidad import pregunta
import json

class Gestor:

    def __init__(self):
        self.preguntas = []


    def validar_datos(self, fila):
    
        campos = [
            "pregunta",
            "opcion_a",
            "opcion_b",
            "opcion_c",
            "opcion_d",
            "respuesta_correcta",
            "dificultad",
            "tema"
        ]

        # Validar campos obligatorios
        for campo in campos:
            if pd.isna(fila[campo]) or fila[campo] == "":
                return False


        # Validar respuesta correcta
        if fila["respuesta_correcta"] not in ["A", "B", "C", "D"]:
            return False


        # Validar dificultad
        if fila["dificultad"] not in ["Fácil", "Media", "Difícil"]:
            return False


        return True



    def convertir_a_objeto(self, fila):
        
        return pregunta(
            id=int(fila["id"]),
            pregunta=fila["pregunta"],
            opcion_a=fila["opcion_a"],
            opcion_b=fila["opcion_b"],
            opcion_c=fila["opcion_c"],
            opcion_d=fila["opcion_d"],
            respuesta_correcta=fila["respuesta_correcta"],
            dificultad=fila["dificultad"],
            tema=fila["tema"]
        )
        
        
    def cargar_desde_csv(self, ruta):
        
        df = pd.read_csv(ruta)


        df = df.rename(columns={
            "ID": "id",
            "Pregunta": "pregunta",
            "OpcionA": "opcion_a",
            "OpcionB": "opcion_b",
            "OpcionC": "opcion_c",
            "OpcionD": "opcion_d",
            "RespuestaCorrecta": "respuesta_correcta",
            "Dificultad": "dificultad",
            "Tema": "tema"
        })
        df.columns = df.columns.str.lower()

        # Adaptar nombres del CSV a la clase pregunta
        df.rename(columns={
            "ID": "id",
            "Pregunta": "pregunta",
            "OpcionA": "opcion_a",
            "OpcionB": "opcion_b",
            "OpcionC": "opcion_c",
            "OpcionD": "opcion_d",
            "RespuestaCorrecta": "respuesta_correcta",
            "Dificultad": "dificultad",
            "Tema": "tema"
        }, inplace=True)


        for _, fila in df.iterrows():
    
            if self.validar_datos(fila):
                objeto = self.convertir_a_objeto(fila)
                self.preguntas.append(objeto)
            else:
                print("Fila rechazada:")
                print(fila.to_dict())
                print("-" * 50)
        
    def cargar_desde_json(self, ruta):
    
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        preguntas = datos["cuestionario"]["preguntas"]

        df = pd.DataFrame(preguntas)

        df["opcion_a"] = df["opciones"].apply(lambda x: x["A"])
        df["opcion_b"] = df["opciones"].apply(lambda x: x["B"])
        df["opcion_c"] = df["opciones"].apply(lambda x: x["C"])
        df["opcion_d"] = df["opciones"].apply(lambda x: x["D"])

        df = df.drop(columns=["opciones"])

        for _, fila in df.iterrows():
            if self.validar_datos(fila):
                p = pregunta(
                    fila["id"],
                    fila["pregunta"],
                    fila["opcion_a"],
                    fila["opcion_b"],
                    fila["opcion_c"],
                    fila["opcion_d"],
                    fila["respuesta_correcta"],
                    fila["dificultad"],
                    fila["tema"]
                )

                self.preguntas.append(p)

        print("Preguntas cargadas desde JSON")
    
    def cargar_desde_txt(self, ruta):
    
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = [l.strip() for l in f.readlines()]

        self.preguntas.clear()

        i = 0

        while i < len(lineas):

            if lineas[i].startswith("ID:"):

                id = int(lineas[i].split(":")[1])

                tema = lineas[i+1].split(":",1)[1].strip()

                dificultad = lineas[i+2].split(":",1)[1].strip()

                pregunta_texto = lineas[i+3].split(":",1)[1].strip()

                opcion_a = lineas[i+6][3:].strip()

                opcion_b = lineas[i+7][3:].strip()

                opcion_c = lineas[i+8][3:].strip()

                opcion_d = lineas[i+9][3:].strip()

                respuesta = lineas[i+11].split(":")[1].strip()
                
    

                p = pregunta(
                    id,
                    pregunta_texto,
                    opcion_a,
                    opcion_b,
                    opcion_c,
                    opcion_d,
                    respuesta,
                    dificultad,
                    tema
                )

                self.preguntas.append(p)

            i += 1

        print("Preguntas cargadas:", len(self.preguntas))