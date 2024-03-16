import math  # Importa el módulo math para usar la función factorial
import numpy as np  # Importa numpy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa matplotlib para trazar gráficos

# Definición de la función que calcula la aproximación del coseno de un ángulo utilizando la serie de Taylor
def func_cos(x, n):
    cos_aprox = 0
    for i in range(n):
        coef = (-1)**i  # Calcula el coeficiente alternante (-1)^i
        num = x**(2*i)   # Calcula el numerador (x^(2*i))
        denom = math.factorial(2*i)  # Calcula el denominador (factorial(2*i))
        cos_aprox += coef * (num / denom)  # Suma el término i-ésimo de la serie de Taylor al resultado
    return cos_aprox

# Crea un array de ángulos en el rango de -2*pi a 2*pi con un paso de 0.1
angulos = np.arange(-2*np.pi, 2*np.pi, 0.1)

# Calcula los valores reales del coseno para cada ángulo en el rango
p_cos = np.cos(angulos)

# Calcula los valores aproximados del coseno utilizando la serie de Taylor con 3 términos para cada ángulo en el rango
t_cos = [func_cos(angle, 3) for angle in angulos]

# Crea una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Grafica la función coseno real y su aproximación utilizando la serie de Taylor con 3 términos
ax.plot(angulos, p_cos)
ax.plot(angulos, t_cos)

# Establece el límite en el eje y para mostrar claramente la diferencia entre las funciones
ax.set_ylim([-5, 5])

# Agrega una leyenda al gráfico
ax.legend(['funcion cos()', 'serie de Taylor - 3 términos'])

# Muestra el gráfico
plt.show()
