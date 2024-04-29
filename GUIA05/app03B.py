import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def newton_raphson(f, x0, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función f(x) utilizando el método de Newton-Raphson.
    
    Parameters:
        f (sympy function): La función para la cual se busca la raíz.
        x0 (float): Aproximación inicial de la raíz.
        tol (float): Tolerancia para el error relativo.
        max_iter (int): Número máximo de iteraciones permitidas.
    
    Returns:
        float: Aproximación de la raíz.
        int: Número de iteraciones realizadas.
    """
    # Derivada de la función
    df = sp.diff(f, 'x')
    
    # Convertir la función y su derivada a funciones lambda
    f_func = sp.lambdify('x', f)
    df_func = sp.lambdify('x', df)
    
    # Inicialización de variables
    x = x0
    iter_count = 0
    
    # Bucle de iteraciones
    while True:
        x_prev = x
        x = x - f_func(x) / df_func(x)
        iter_count += 1
        
        # Verificar convergencia
        if abs((x - x_prev) / x) < tol or iter_count >= max_iter:
            break
    
    return x, iter_count

# Funciones dadas
x = sp.symbols('x')
f1 = sp.exp(-x) - sp.ln(x)
f2 = x**2 - 0.5

# Aproximaciones iniciales
x0_f1 = 0.5
x0_f2 = 0.5

# Encuentra las raíces utilizando el método de Newton-Raphson
root_f1, iter_count_f1 = newton_raphson(f1, x0_f1)
root_f2, iter_count_f2 = newton_raphson(f2, x0_f2)

print("Raíz de f(x) = e**-x - ln(x):", root_f1)
print("Iteraciones necesarias:", iter_count_f1)
print("Raíz de f(x) = x**2 - 0.5:", root_f2)
print("Iteraciones necesarias:", iter_count_f2)

# Intervalo para graficar
x_values = np.linspace(0.1, 5, 1000)

# Convertir las funciones a funciones lambda para graficar
f1_lambda = sp.lambdify(x, f1)
f2_lambda = sp.lambdify(x, f2)

# Graficar las funciones
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, f1_lambda(x_values), label="$e^{-x} - \ln(x)$")
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función 1')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, f2_lambda(x_values), label="$x^2 - 0.5$")
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Función 2')
plt.legend()

plt.tight_layout()
plt.show()
