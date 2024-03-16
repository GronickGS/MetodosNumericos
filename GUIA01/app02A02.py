# Comienza un bucle infinito que solicita continuamente al usuario que ingrese un número decimal
while True:
    # Solicita al usuario que ingrese un número decimal
    num = input("Ingresa decimal: ")
    # Verifica si el usuario ingresó 'x', en cuyo caso se rompe el bucle
    if num == 'x':
        break
    else:
        # Imprime la representación binaria del número decimal ingresado por el usuario
        print(bin(int(num)))
