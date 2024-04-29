import sympy as sp

def biseccion(f, xi, xs, tol=0.01):
    """
    Encuentra la raíz de la función f(x) en el intervalo [xi, xs] utilizando el método de la bisección.
    
    Parameters:
        f (sympy function): Función a evaluar.
        xi (float): Extremo izquierdo del intervalo inicial.
        xs (float): Extremo derecho del intervalo inicial.
        tol (float): Tolerancia para el error aproximado.
    
    Returns:
        float: Aproximación de la raíz de la función.
    """
    # Inicialización del error aproximado
    ea = 100
    
    # Bucle de iteraciones
    while ea > tol:
        # Calcula la raíz aproximada
        xr = (xi + xs) / 2
        
        # Evalúa la función en los extremos del intervalo y en la raíz aproximada
        f_xi = f.subs('x', xi)
        f_xs = f.subs('x', xs)
        f_xr = f.subs('x', xr)
        
        # Determina en qué sub-intervalo se encuentra la raíz
        if f_xi * f_xr < 0:
            xs = xr
        elif f_xs * f_xr < 0:
            xi = xr
        else:
            return xr  # Si f(xi)*f(xs) == 0, xr es la raíz
        
        # Calcula el error aproximado
        xr_anterior = xr
        xr = (xi + xs) / 2
        ea = abs((xr - xr_anterior) / xr) * 100
        
    return xr

# Definición de la variable simbólica x
x = sp.symbols('x')

# Define la función f(x)
f = x**2 - 4

# Intervalo inicial
xi = -2
xs = 2

# Encuentra la raíz de la función en el intervalo [xi, xs]
raiz = biseccion(f, xi, xs)

print("La raíz aproximada es:", raiz)
