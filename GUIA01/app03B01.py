# Definición de la función BinarioADecima1 que convierte un número binario en decimal
def BinarioADecima1(binario):
    # Inicializa las variables decimal e i a 0
    decimal, i = 0, 0
    # Bucle while que se ejecuta hasta que el número binario no sea igual a 0
    while(binario != 0):
        # Obtiene el último dígito del número binario
        dec = binario % 10
        # Calcula el valor decimal del dígito actual y lo suma al resultado
        decimal = decimal + dec * pow(2, i)
        # Divide el número binario por 10 para eliminar el último dígito
        binario = binario // 10
        # Incrementa el exponente para la siguiente posición binaria
        i += 1
    # Imprime el resultado decimal
    print(decimal)

# Llamadas a la función para convertir números binarios a decimales
BinarioADecima1(100)    #Este es el número binario "100", que es 4 en decimal.
BinarioADecima1(101)    # Este es el número binario "101", que es 5 en decimal.
BinarioADecima1(10011110101010111111111)    # Este es un número binario muy grande. Su equivalente decimal es 252246015.
