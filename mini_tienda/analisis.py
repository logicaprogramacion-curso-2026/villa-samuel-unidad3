# analisis.py

import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ARCHIVO_CSV = "ventas.csv"


def cargar_dataframe():
    """
    Carga las ventas desde ventas.csv.
    """

    if not os.path.exists(ARCHIVO_CSV):
        return pd.DataFrame()

    try:
        df = pd.read_csv(ARCHIVO_CSV)

    except Exception:
        return pd.DataFrame()

    return df


def ingresos_por_producto():
    """
    Agrupa los ingresos por producto usando Pandas.
    """

    df = cargar_dataframe()

    if df.empty:
        return pd.DataFrame()

    resultado = (
        df.groupby("producto")["total"]
        .sum()
        .reset_index()
    )

    return resultado


def calcular_metricas():
    """
    Calcula estadísticas utilizando NumPy.
    """

    df = cargar_dataframe()

    if df.empty:
        return {
            "media": 0,
            "desviacion": 0,
            "suma": 0
        }

    valores = np.array(
        df["total"],
        dtype=float
    )

    media = np.mean(valores)

    desviacion = np.std(valores)

    suma = np.sum(valores)

    return {
        "media": media,
        "desviacion": desviacion,
        "suma": suma
    }


def generar_grafico():
    """
    Muestra una gráfica de barras
    con los ingresos por producto.
    """

    datos = ingresos_por_producto()

    if datos.empty:
        return False

    plt.figure(figsize=(8, 5))

    plt.bar(
        datos["producto"],
        datos["total"]
    )

    plt.title(
        "Ingresos por producto"
    )

    plt.xlabel(
        "Producto"
    )

    plt.ylabel(
        "Ingresos ($)"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    plt.show()

    return True


def exportar_grafico():
    """
    Guarda la gráfica como ingresos.png.
    """

    datos = ingresos_por_producto()

    if datos.empty:
        return False

    plt.figure(figsize=(8, 5))

    plt.bar(
        datos["producto"],
        datos["total"]
    )

    plt.title(
        "Ingresos por producto"
    )

    plt.xlabel(
        "Producto"
    )

    plt.ylabel(
        "Ingresos ($)"
    )

    plt.xticks(
        rotation=30
    )

    plt.tight_layout()

    plt.savefig(
        "ingresos.png"
    )

    plt.close()

    return True