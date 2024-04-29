# 5. DESARROLLO DE LA PRACTICA
# A. Implementa el método numérico de Gauss Jordan en Python de manera que acepte
# cualquier sistema de ecuaciones como dato de entrada en consola.

import numpy as np

def gauss_jordan(A, b):
    """
    Implementación del método numérico de Gauss-Jordan para resolver un sistema de ecuaciones lineales Ax=b.

    Args:
    A (numpy.ndarray): La matriz de coeficientes del sistema.
    b (numpy.ndarray): El vector de términos constantes.

    Returns:
    numpy.ndarray: La solución del sistema de ecuaciones.
    """
    n = len(A)
    Ab = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(Ab[j, i]) > abs(Ab[pivot_row, i]):
                pivot_row = j
        Ab[[i, pivot_row]] = Ab[[pivot_row, i]]
        
        for j in range(i + 1, n):
            Ab[j] -= Ab[i] * (Ab[j, i] / Ab[i, i])

    for i in range(n - 1, -1, -1):
        Ab[i] /= Ab[i, i]
        for j in range(i - 1, -1, -1):
            Ab[j] -= Ab[i] * Ab[j, i]

    return Ab[:, -1]

def main():
    n = int(input("Ingrese el número de incógnitas: "))
    print("Ingrese los coeficientes de la matriz de coeficientes A:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f'A[{i+1}][{j+1}]='))
    print("Ingrese el vector de términos constantes b:")
    b = np.zeros(n)
    for i in range(n):
        b[i] = float(input(f'b[{i+1}]='))
    
    x = gauss_jordan(A, b)
    print("\nLa solución del sistema de ecuaciones es:")
    for i in range(len(x)):
        print(f'x[{i+1}] = {x[i]}')

if __name__ == "__main__":
    main()
