import math  # Importa el módulo math para usar la función factorial y radians

# Definición de la función que calcula la aproximación del coseno de un ángulo utilizando la serie de Maclaurin
def func_cos(x, n):
    cos_aprox = 0
    for i in range(n):
        coef = (-1)**i  # Calcula el coeficiente alternante (-1)^i
        num = x**(2*i)   # Calcula el numerador (x^(2*i))
        denom = math.factorial(2*i)  # Calcula el denominador (factorial(2*i))
        cos_aprox += coef * (num / denom)  # Suma el término i-ésimo de la serie de Maclaurin al resultado
    return cos_aprox

# Convierte el ángulo de 45 grados a radianes
angulo_rad = math.radians(45)

# Calcula la aproximación del coseno del ángulo con 5 términos de la serie de Maclaurin
out = func_cos(angulo_rad, 5)

# Imprime el resultado de la aproximación del coseno
print(out)
