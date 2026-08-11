import pandas as pd

# Leer el archivo CSV
ventas = pd.read_csv(r"C:\Users\savillaro\Downloads\ldp\deber_4\ventas.csv")

# Calcular el ingreso por producto
ventas["Ingreso"] = ventas["Cantidad"] * ventas["Precio"]

# Mostrar la tabla completa
print("=== Ventas ===")
print(ventas)

# Calcular el ingreso total
ingreso_total = ventas["Ingreso"].sum()

print("\nIngreso total:", ingreso_total)