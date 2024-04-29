import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2) - x

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Implementación del método de la secante para encontrar una raíz de la función f(x).

    Args:
    f (function): La función para la cual se busca la raíz.
    x0 (float): Primer punto inicial.
    x1 (float): Segundo punto inicial.
    tol (float): Tolerancia para la convergencia.
    max_iter (int): Número máximo de iteraciones permitidas.

    Returns:
    float: La aproximación de la raíz de la función.
    """
    iteration = 0
    while iteration < max_iter:
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_next - x1) < tol:
            return x_next
        x0, x1 = x1, x_next
        iteration += 1
    print("El método de la secante no converge después de", max_iter, "iteraciones.")
    return None

# Graficamos la función para visualizar los puntos iniciales
x_values = np.linspace(-2, 2, 400)
y_values = f(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='f(x) = e^(-x^2) - x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de la función f(x)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()

# Realizamos el método de la secante para encontrar la raíz
x0 = -1
x1 = 1
root = secant_method(f, x0, x1)
if root is not None:
    print("La raíz encontrada es:", root)
else:
    print("No se pudo encontrar una raíz.")
