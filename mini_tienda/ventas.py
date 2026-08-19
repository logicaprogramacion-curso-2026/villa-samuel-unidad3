# ventas.py

from datetime import datetime
import random

from datos import (
    PRECIOS,
    STOCK,
    producto_existe,
    obtener_nombre
)


def calcular_descuento(unidades, subtotal):
    """
    Aplica 5% de descuento cuando
    se compran 10 unidades o más.
    """

    if unidades >= 10:

        descuento = subtotal * 0.05

    else:

        descuento = 0

    return descuento


def registrar_venta(producto_id, unidades):
    """
    Registra una venta individual.
    """

    if not producto_existe(producto_id):

        return None, "El producto no existe."

    if unidades <= 0:

        return None, "La cantidad debe ser mayor que cero."

    if unidades > STOCK[producto_id]:

        return None, "No existe suficiente stock."

    precio = PRECIOS[producto_id]

    subtotal = precio * unidades

    descuento = calcular_descuento(
        unidades,
        subtotal
    )

    total = subtotal - descuento

    STOCK[producto_id] -= unidades

    venta = {
        "fecha": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "producto_id": producto_id,
        "producto": obtener_nombre(producto_id),
        "unidades": unidades,
        "precio_unitario": precio,
        "subtotal": subtotal,
        "descuento": descuento,
        "total": total
    }

    return venta, "Venta registrada correctamente."


def generar_ventas_prueba(cantidad=10):
    """
    Genera ventas de prueba.

    Utiliza:
    for
    if
    continue
    break
    """

    ventas_generadas = []

    productos = list(PRECIOS.keys())

    for i in range(cantidad):

        if i >= 20:

            break

        producto_id = random.choice(
            productos
        )

        unidades = random.randint(
            1,
            15
        )

        venta, mensaje = registrar_venta(
            producto_id,
            unidades
        )

        if venta is None:

            continue

        ventas_generadas.append(
            venta
        )

    return ventas_generadas