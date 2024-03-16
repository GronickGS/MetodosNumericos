import math  # Importa el módulo math para usar la función factorial

# Definición de la función que calcula la aproximación de la función exponencial e^x utilizando la serie de Taylor
def func_e(x, n):
    e_aprox = 0
    for i in range(n):
        # Calcula el i-ésimo término de la serie y lo agrega a la aproximación de e^x
        e_aprox += x**i / math.factorial(i)
    return e_aprox

x = 5  # Valor de x para el cual se calcularán las aproximaciones de e^x

# Itera sobre diferentes números de términos en la serie de Taylor
for i in range(1, 11):  # Empezando desde 1 término hasta 10 términos
    # Calcula la aproximación de e^x con i términos de la serie de Taylor
    e_aprox = func_e(x, i)
    # Calcula el valor real de e^x utilizando la función exp del módulo math
    e_exp = math.exp(x)
    # Calcula el error absoluto entre la aproximación y el valor real
    e_error = abs(e_aprox - e_exp)
    # Imprime el número de términos, la aproximación, el valor real y el error absoluto
    print(f'{i} términos: Serie de Taylor aproximada = {e_aprox}, exponencial calculada = {e_exp}, error: {e_error}')
