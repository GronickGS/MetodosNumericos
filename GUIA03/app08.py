import math  # Importa el módulo math para usar la función factorial
import numpy as np  # Importa numpy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa matplotlib para trazar gráficos

# Definición de la función que calcula la aproximación del coseno de un ángulo utilizando la serie de Taylor
def func_sin(x, n):
    sin_aprox = 0
    for i in range(n):
        coef = (-1)**i  # Calcula el coeficiente alternante (-1)^i
        num = x**(2*i)   # Calcula el numerador (x^(2*i))
        denom = math.factorial(2*i)  # Calcula el denominador (factorial(2*i))
        sin_aprox += coef * (num / denom)  # Suma el término i-ésimo de la serie de Taylor al resultado
    return sin_aprox

# Crea un array de ángulos en el rango de -2*pi a 2*pi con un paso de 0.1
angulos = np.arange(-2*np.pi, 2*np.pi, 0.1)

# Calcula los valores reales del coseno para cada ángulo en el rango
p_sin = np.sin(angulos)

# Crea una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Grafica la función coseno real
ax.plot(angulos, p_sin)

# Calcula y grafica las aproximaciones del coseno utilizando la serie de Taylor con diferentes cantidades de términos
for i in range(1, 6):  # Itera de 1 a 5 términos
    t_sin = [func_sin(angulo, i) for angulo in angulos]  # Calcula los valores aproximados para la serie de Taylor con i términos
    ax.plot(angulos, t_sin)  # Grafica la aproximación

# Establece el límite en el eje y para mostrar claramente la diferencia entre las funciones
ax.set_ylim([-7, 4])

# Crea una lista de leyendas para cada serie de Taylor
legend_lst = ['funcion sin()']
for i in range(1, 6):  # Itera de 1 a 5 términos
    legend_lst.append(f'Serie de Taylor - {i} términos')

# Agrega una leyenda al gráfico en la esquina inferior izquierda
ax.legend(legend_lst, loc=3)

# Muestra el gráfico
plt.show()
