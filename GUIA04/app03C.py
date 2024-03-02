'''
Una vez que tenemos nuestra matriz,
podemos empezar a realizar operaciones 
básicas como la suma, la resta, la 
multiplicación y la división. Por ejemplo, 
para sumar dos matrices, podemos usar 
la función numpy.add(). Veamos un ejemplo:
'''

import numpy as np

# Creamos las matrices
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

# Calculamos la suma de las matrices
suma = np.add(matriz1, matriz2)

# Imprimimos la suma
print(suma)
