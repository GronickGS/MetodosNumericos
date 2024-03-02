def signo_magnitud(numero, bits):
    if numero >= 0:
        return bin(numero)[2:].zfill(bits)
    else:
        return '1' + bin(abs(numero))[2:].zfill(bits - 1)

def complemento_uno(numero, bits):
    if numero >= 0:
        return bin(numero)[2:].zfill(bits)
    else:
        binario = bin(abs(numero) - 1)[2:].zfill(bits)
        complemento = ''.join('1' if bit == '0' else '0' for bit in binario)
        return complemento

def complemento_dos(numero, bits):
    if numero >= 0:
        return bin(numero)[2:].zfill(bits)
    else:
        binario = bin(abs(numero))[2:].zfill(bits)
        invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
        complemento = bin(int(invertido, 2) + 1)[2:].zfill(bits)
        return complemento

if __name__ == "__main__":
    numero = int(input("Ingrese un número entero: "))
    bits = int(input("Ingrese la cantidad de bits: "))

    print("Signo-Magnitud:", signo_magnitud(numero, bits))
    print("Complemento a uno:", complemento_uno(numero, bits))
    print("Complemento a dos:", complemento_dos(numero, bits))
