import numpy as np

# Creamos la matriz
matrix = np.array([[2, 1], [3, 4]])

# Calculamos la inversa de la matriz
inverse_matrix = np.linalg.inv(matrix)

# Imprimimos la matriz original y su inversa
print("Original:")
print(matrix)
print("\nMatriz inversa:")
print(inverse_matrix)
