import pandas as pd

estudiantes = pd.read_csv(r"C:\Users\savillaro\Downloads\ldp\deber_4_2\notas.csv")

aprobados = estudiantes[estudiantes["Nota"] >= 7]

print("=== Estudiantes aprobados ===")
print(aprobados)

promedio = estudiantes["Nota"].mean()

print("\nPromedio del curso:", round(promedio, 2))
print("Nota más alta:", estudiantes["Nota"].max())
print("Nota más baja:", estudiantes["Nota"].min())