import numpy as np

# Definimos la matriz
matrix = np.array([[2, 1], [3, 4]])

# Calculamos el determinante de la matriz
determinante = np.linalg.det(matrix)

# Imprimimos la matriz y su determinante
print("Matriz:")
print(matrix)
print("\nDeterminante:")
print(determinante)
