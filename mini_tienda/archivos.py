# archivos.py

import csv
import os


ARCHIVO_CSV = "ventas.csv"
ARCHIVO_LOG = "log.txt"


def guardar_venta_csv(venta):
    """
    Guarda una venta en ventas.csv.
    """

    archivo_existe = os.path.exists(
        ARCHIVO_CSV
    )

    with open(
        ARCHIVO_CSV,
        "a",
        newline="",
        encoding="utf-8"
    ) as archivo:

        campos = [
            "fecha",
            "producto_id",
            "producto",
            "unidades",
            "precio_unitario",
            "subtotal",
            "descuento",
            "total"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        if not archivo_existe:

            escritor.writeheader()

        escritor.writerow(venta)


def registrar_log(mensaje):
    """
    Registra mensajes en log.txt.
    """

    with open(
        ARCHIVO_LOG,
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            mensaje + "\n"
        )


def cargar_ventas_csv():
    """
    Lee las ventas desde ventas.csv.

    Controla el caso donde el archivo
    todavía no existe.
    """

    try:

        with open(
            ARCHIVO_CSV,
            "r",
            newline="",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(
                archivo
            )

            datos = list(lector)

    except FileNotFoundError:

        return []

    else:

        return datos

    finally:

        pass