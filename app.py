# Se establece el valor inicial de RegA
RegA = 0xce5

# Desplazamiento de RegA hacia la derecha en 2 bits y operación AND
if (RegA >> 1) & 1:
    RegB = 0x4b
else:
    RegB = 0x41

# Operación OR para establecer el cuarto bit de RegB en 1
RegB |= 1<< 7

# Operación AND bit a bit para poner el tercer bit de RegB en 0
RegB &= ~(1 << 1)

# Mostrar el valor final de RegB
print("El valor de RegB es:", hex(RegB))