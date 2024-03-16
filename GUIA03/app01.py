import math  # Importa el módulo math para usar la función factorial

x = 2  # Define el valor de x como 2

# Calcula la aproximación de e^2 utilizando la serie de Maclaurin
# e^2 = x^0/0! + x^1/1! + x^2/2! + x^3/3! + x^4/4! + x^2/2!
e_a_la_2 = (
    x**0 / math.factorial(0) +  # Primer término: x^0/0!
    x**1 / math.factorial(1) +  # Segundo término: x^1/1!
    x**2 / math.factorial(2) +  # Tercer término: x^2/2!
    x**3 / math.factorial(3) +  # Cuarto término: x^3/3!
    x**4 / math.factorial(4) +  # Quinto término: x^4/4!
    x**2 / math.factorial(2)    # Sexto término: x^2/2! (se repite)
)

# Imprime el resultado de la aproximación de e^2
print(e_a_la_2)
