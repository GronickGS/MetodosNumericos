'''
Utilizando tus métodos anteriormente implementados, resuelve el siguiente problema: 
Se nos da un valor aproximado de π que es 22/7 = 3,1428571 y el valor verdadero es 
3,1415926. ¿Calcular error absoluto, relativo y porcentual?
'''

def error_absoluto(valor_real, valor_aproximado):
    return abs(valor_real - valor_aproximado)

def error_relativo(valor_real, valor_aproximado):
    if valor_real != 0:
        return abs(valor_real - valor_aproximado) / abs(valor_real)
    else:
        return "No se puede calcular el error relativo porque el valor real es cero."

def error_porcentual(valor_real, valor_aproximado):
    if valor_real != 0:
        return abs(valor_real - valor_aproximado) / abs(valor_real) * 100
    else:
        return "No se puede calcular el error porcentual porque el valor real es cero."


# Valores proporcionados
valor_verdadero_pi = 3.1415926
valor_aproximado_pi = 22 / 7

# Cálculo de errores
error_abs = error_absoluto(valor_verdadero_pi, valor_aproximado_pi)
error_rel = error_relativo(valor_verdadero_pi, valor_aproximado_pi)
error_porcent = error_porcentual(valor_verdadero_pi, valor_aproximado_pi)

# Mostrar resultados
print("Error Absoluto:", error_abs)
print("Error Relativo:", error_rel)
print("Error Porcentual:", error_porcent)
