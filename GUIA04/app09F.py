# Producto escalar y vectorial de vectores

import numpy as np

# Definimos los vectores
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Calculamos el producto escalar
producto_escalar = np.dot(vector_a, vector_b)
print("Producto Escalar:", producto_escalar)

# Calculamos el producto vectorial
producto_vectorial = np.cross(vector_a, vector_b)
print("Producto Vectorial:", producto_vectorial)
