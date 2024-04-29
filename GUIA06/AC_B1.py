# Implementar en Python el método de Regula Falsi, con su respectivo grafico inicial. Y
# verifica su correcto funcionamiento con los dos ejercicios resueltos visto en clase:

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3

def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    """
    Implementación del método de la regula falsi para encontrar una raíz de la función f(x).

    Args:
    f (function): La función para la cual se busca la raíz.
    a (float): Extremo izquierdo del intervalo inicial.
    b (float): Extremo derecho del intervalo inicial.
    tol (float): Tolerancia para la convergencia.
    max_iter (int): Número máximo de iteraciones permitidas.

    Returns:
    float: La aproximación de la raíz de la función.
    """
    if f(a) * f(b) >= 0:
        print("El método de la regula falsi no es aplicable en este intervalo.")
        return None

    iteration = 0
    while iteration < max_iter:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    print("El método de la regula falsi no converge después de", max_iter, "iteraciones.")
    return None

# Graficamos la función para visualizar el intervalo inicial
x_values = np.linspace(-2, 4, 400)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de la función f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

# Realizamos el método de la regula falsi para encontrar la raíz
a = 1
b = 2
root = regula_falsi(f, a, b)
if root is not None:
    print("La raíz encontrada es:", root)
else:
    print("No se pudo encontrar una raíz.")
