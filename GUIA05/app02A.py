import numpy as np
import matplotlib.pyplot as plt

def bisection(f, xi, xs, tol=1e-6, max_iter=100):
    """
    Implementación del método de la bisección para encontrar la raíz de la función f(x) en el intervalo [xi, xs].
    
    Parámetros:
        f (función): Función para la cual se busca la raíz.
        xi (float): Extremo izquierdo del intervalo.
        xs (float): Extremo derecho del intervalo.
        tol (float): Tolerancia para el error aproximado. El algoritmo se detendrá cuando el tamaño del intervalo sea menor que tol.
        max_iter (int): Número máximo de iteraciones permitidas.
        
    Retorna:
        float: Aproximación de la raíz de la función f(x).
    """
    # Inicialización de variables
    iter_count = 0
    ea = float('inf')
    
    # Bucle de iteración
    while ea > tol and iter_count < max_iter:
        xr = (xi + xs) / 2  # Calcula la aproximación de la raíz
        
        if f(xi) * f(xr) < 0:
            xs = xr  # La raíz está en el subintervalo izquierdo
        elif f(xr) * f(xs) < 0:
            xi = xr  # La raíz está en el subintervalo derecho
        else:
            break  # La raíz es xr
        
        if iter_count > 0:
            ea = np.abs((xr - xr_prev) / xr) * 100  # Calcula el error aproximado
            
        xr_prev = xr
        iter_count += 1
    
    return xr

# Definición de la primera función
def f1(x):
    return np.exp(-x) - np.log(x)

# Definición de la segunda función
def f2(x):
    return x**2 - 0.5

# Graficar la primera función
x_values = np.linspace(0.1, 2, 400)
y_values = f1(x_values)
plt.plot(x_values, y_values, label='$f(x) = e^{-x} - \ln(x)$')

# Graficar la segunda función
x_values = np.linspace(0.1, 2, 400)
y_values = f2(x_values)
plt.plot(x_values, y_values, label='$f(x) = x^2 - 0.5$')

# Configurar la apariencia del gráfico
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráficos de las funciones')
plt.legend()

# Mostrar el gráfico inicial
plt.show()

# Intervalos iniciales para cada función
intervalos = [((0.1, 0.5), (1.5, 2)),  # Para la función f1
              ((0.1, 0.8), (0.8, 2))]  # Para la función f2

# Calcular y mostrar las raíces aproximadas
for i, intervalo in enumerate(intervalos, start=1):
    print(f"Para la función f{i}:")
    for j, (xi, xs) in enumerate(intervalo, start=1):
        raiz = bisection(eval(f'f{i}'), xi, xs)
        print(f"\tIntervalo {j}: {xi}, {xs} -> Raíz aproximada: {raiz}")
