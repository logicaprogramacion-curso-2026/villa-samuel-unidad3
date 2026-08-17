# archivos.py

import csv
import os


ARCHIVO_CSV = "ventas.csv"
ARCHIVO_LOG = "log.txt"


def guardar_venta_csv(venta):
    """
    Guarda una venta en ventas.csv.
    """

    archivo_existe = os.path.exists(ARCHIVO_CSV)

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
    Guarda mensajes y errores en log.txt.
    """

    with open(
        ARCHIVO_LOG,
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(mensaje + "\n")


def cargar_ventas_csv():
    """
    Lee las ventas almacenadas en el CSV.
    """

    if not os.path.exists(ARCHIVO_CSV):
        return []

    with open(
        ARCHIVO_CSV,
        "r",
        newline="",
        encoding="utf-8"
    ) as archivo:

        lector = csv.DictReader(archivo)

        return list(lector)