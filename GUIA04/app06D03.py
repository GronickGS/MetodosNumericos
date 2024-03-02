import numpy as np
# Definimos las matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
# Realizamos la multiplicación de matrices
result = np.dot(matrix_a, matrix_b)
# Imprimimos las matrices y el resultado de la multiplicación
print("Matriz A:")
print(matrix_a)
print("\nMatriz B:")
print(matrix_b)
print("\nResultado de la multiplicación:")
print(result)
