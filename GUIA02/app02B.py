'''
Implementa tres métodos en Python para calcular el error absoluto,
error relativo y error porcentual y prueba con tres ejemplos.
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

# Ejemplos de prueba
if __name__ == "__main__":
    # Ejemplo 1
    valor_real_1 = 10
    valor_aproximado_1 = 9.5
    print("Ejemplo 1:")
    print("Error Absoluto:", error_absoluto(valor_real_1, valor_aproximado_1))
    print("Error Relativo:", error_relativo(valor_real_1, valor_aproximado_1))
    print("Error Porcentual:", error_porcentual(valor_real_1, valor_aproximado_1))
    print()

    # Ejemplo 2
    valor_real_2 = 5.25
    valor_aproximado_2 = 5.3
    print("Ejemplo 2:")
    print("Error Absoluto:", error_absoluto(valor_real_2, valor_aproximado_2))
    print("Error Relativo:", error_relativo(valor_real_2, valor_aproximado_2))
    print("Error Porcentual:", error_porcentual(valor_real_2, valor_aproximado_2))
    print()

    # Ejemplo 3
    valor_real_3 = 7
    valor_aproximado_3 = 7.5
    print("Ejemplo 3:")
    print("Error Absoluto:", error_absoluto(valor_real_3, valor_aproximado_3))
    print("Error Relativo:", error_relativo(valor_real_3, valor_aproximado_3))
    print("Error Porcentual:", error_porcentual(valor_real_3, valor_aproximado_3))
