# Función para representar un número en signo-magnitud
def signo_magnitud(numero, bits):
    # Si el número es positivo o cero
    if numero >= 0:
        # Convierte el número a binario y rellena con ceros a la izquierda para alcanzar la cantidad de bits
        return bin(numero)[2:].zfill(bits)
    else:  # Si el número es negativo
        # Convierte el valor absoluto del número a binario y rellena con ceros a la izquierda para alcanzar bits-1
        # Agrega un bit de signo '1' al principio para indicar que es negativo
        return '1' + bin(abs(numero))[2:].zfill(bits - 1)

# Función para representar un número en complemento a uno
def complemento_uno(numero, bits):
    # Si el número es positivo o cero
    if numero >= 0:
        # Convierte el número a binario y rellena con ceros a la izquierda para alcanzar la cantidad de bits
        return bin(numero)[2:].zfill(bits)
    else:  # Si el número es negativo
        # Obtiene el complemento a uno del valor absoluto del número
        binario = bin(abs(numero) - 1)[2:].zfill(bits)
        # Invierte cada bit en la representación binaria para obtener el complemento a uno
        complemento = ''.join('1' if bit == '0' else '0' for bit in binario)
        return complemento

# Función para representar un número en complemento a dos
def complemento_dos(numero, bits):
    # Si el número es positivo o cero
    if numero >= 0:
        # Convierte el número a binario y rellena con ceros a la izquierda para alcanzar la cantidad de bits
        return bin(numero)[2:].zfill(bits)
    else:  # Si el número es negativo
        # Obtiene el complemento a uno del valor absoluto del número
        binario = bin(abs(numero))[2:].zfill(bits)
        # Invierte cada bit en la representación binaria para obtener el complemento a uno
        invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
        # Suma uno al complemento a uno para obtener el complemento a dos
        complemento = bin(int(invertido, 2) + 1)[2:].zfill(bits)
        return complemento

# Si el script se ejecuta directamente
if __name__ == "__main__":
    # Solicita al usuario un número entero y la cantidad de bits
    numero = int(input("Ingrese un número entero: "))
    bits = int(input("Ingrese la cantidad de bits: "))

    # Muestra las representaciones binarias utilizando los tres esquemas mencionados
    print("Signo-Magnitud:", signo_magnitud(numero, bits))
    print("Complemento a uno:", complemento_uno(numero, bits))
    print("Complemento a dos:", complemento_dos(numero, bits))
