# ejemplo 1 (Cálculo del promedio de calificaciones de estudiantes)


import numpy as np

notas = np.array([8.5, 9.2, 7.8, 10, 8.9])

promedio = np.mean(notas)

print("Notas:", notas)

print("Promedio:", promedio)
 

# ejemplo 2 (Cálculo de ventas mensuales)

import numpy as np

ventas = np.array([1200, 1500, 1700, 1400, 2100, 1800])

print("Total de ventas:", np.sum(ventas))

print("Promedio:", np.mean(ventas))

print("Venta máxima:", np.max(ventas))



matriz = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(matriz[0, 0])
print(matriz[1, 2])