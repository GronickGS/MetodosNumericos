import math  # Importa el módulo math para usar la función factorial

def func_e(x, n):
    e_aprox = 0  # Inicializa la variable para almacenar la aproximación de e
    for i in range(n):  # Itera sobre los primeros n términos de la serie de Maclaurin
        e_aprox += x**i / math.factorial(i)  # Calcula el i-ésimo término de la serie y lo agrega a la aproximación de e
    return e_aprox  # Devuelve la aproximación de e

# Llama a la función func_e con x=2 y n=10 para obtener una aproximación de e^2 con 10 términos de la serie de Maclaurin
out = func_e(2, 10)
print(out)  # Imprime el resultado de la aproximación de e^2
