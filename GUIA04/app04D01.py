'''
Por supuesto, las operaciones que podemos realizar
con matrices en NumPy son mucho más complejas que 
simples sumas o restas. Por ejemplo, podemos calcular 
la transpuesta de una matriz usando la función 
numpy.transpose(), o calcular su inversa usando la 
función numpy.linalg.inv(). También podemos multiplicar 
dos matrices usando la función numpy.dot(), o calcular 
su determinante usando la función numpy.linalg.det().
'''

import numpy as np
# Creamos la matriz
arr = np.array([[1, 2, 3], [4, 5, 6]])
# Calculamos la transposición de la matriz
transposed_arr = np.transpose(arr)
# Imprimimos la matriz original y la matriz transpuesta
print("Arreglo original:")
print(arr)
print("\nArreglo transpuesto:")
print(transposed_arr)
