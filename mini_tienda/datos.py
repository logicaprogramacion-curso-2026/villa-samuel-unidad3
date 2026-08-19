# datos.py

# Catálogo utilizando una tupla
CATALOGO = (
    ("P001", "Arroz"),
    ("P002", "Azúcar"),
    ("P003", "Leche"),
    ("P004", "Aceite"),
    ("P005", "Pan"),
)

# Diccionario de precios
PRECIOS = {
    "P001": 1.25,
    "P002": 1.10,
    "P003": 0.95,
    "P004": 2.50,
    "P005": 0.50,
}

# Diccionario de stock
STOCK = {
    "P001": 30,
    "P002": 25,
    "P003": 20,
    "P004": 15,
    "P005": 40,
}


def obtener_nombre(producto_id):

    for codigo, nombre in CATALOGO:

        if codigo == producto_id:
            return nombre

    return None


def producto_existe(producto_id):

    return obtener_nombre(producto_id) is not None


def obtener_productos():

    return CATALOGO


def agregar_producto(
    producto_id,
    nombre,
    precio,
    stock
):
    """
    Agrega un nuevo producto al catálogo.

    Reto A.
    """

    global CATALOGO

    if producto_existe(producto_id):

        return False

    nuevo_producto = (
        producto_id,
        nombre
    )

    CATALOGO = CATALOGO + (
        nuevo_producto,
    )

    PRECIOS[producto_id] = precio

    STOCK[producto_id] = stock

    return True