# Implementa el método numérico para calcular las matrices de factorizacion L y U en
# Python de manera que acepte cualquier sistema de ecuaciones como datos de entrada
# en la consola. Que se imprime la matriz L y la matriz U resultante.

import numpy as np

def lu_decomposition(A):
    """
    Implementación del método numérico para calcular las matrices de factorización LU.

    Args:
    A (numpy.ndarray): La matriz de coeficientes del sistema.

    Returns:
    numpy.ndarray: La matriz L de la factorización LU.
    numpy.ndarray: La matriz U de la factorización LU.
    """
    n = len(A)
    L = np.zeros((n, n))
    U = np.copy(A)

    for i in range(n):
        L[i, i] = 1

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j] -= factor * U[i]

    return L, U

def main():
    n = int(input("Ingrese el número de incógnitas: "))
    print("Ingrese los coeficientes de la matriz de coeficientes A:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f'A[{i+1}][{j+1}]='))
    
    L, U = lu_decomposition(A)
    
    print("\nLa matriz L resultante es:")
    print(L)
    print("\nLa matriz U resultante es:")
    print(U)

if __name__ == "__main__":
    main()
