'''
Para seleccionar solo la primera fila de la matriz y la segunda columna por ejemplo, podemos hacer:
'''

import numpy as np

# Definimos la matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extraemos la primera fila y la segunda columna
primera_fila = matriz[0, :]
segunda_columna = matriz[:, 1]

# Imprimimos la primera fila y la segunda columna
print("Primera fila:")
print(primera_fila)
print("Segunda columna:")
print(segunda_columna)
