def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f'{clave}: {opciones[clave][0]}')

def leer_opcion(opciones):
    while True:
        opcion = input('Opción: ')
        if opcion in opciones:
            return opcion
        else:
            print('Opción incorrecta, vuelva a intentarlo.')

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ("Suma de dos números binarios enteros", suma_binarios),
        '2': ("Multiplicación de dos números hexadecimales", multiplicacion_hex),
        '3': ("Conversión de Hexadecimal a Octal", conversion_hex_oct),
        '4': ("Resta de dos números octales", resta_octales),
        '5': ("Salir", salir),
    }
    generar_menu(opciones, '5')

def suma_binarios():
    num1 = input("Ingrese el primer número binario: ")
    num2 = input("Ingrese el segundo número binario: ")

    try:
        suma = bin(int(num1, 2) + int(num2, 2))
        print("La suma de", num1, "y", num2, "es:", suma)
    except ValueError:
        print("Por favor, ingrese números binarios válidos.")

def multiplicacion_hex():
    num1 = input("Ingrese el primer número hexadecimal: ")
    num2 = input("Ingrese el segundo número hexadecimal: ")

    try:
        producto = hex(int(num1, 16) * int(num2, 16))
        print("El producto de", num1, "y", num2, "es:", producto)
    except ValueError:
        print("Por favor, ingrese números hexadecimales válidos.")

def conversion_hex_oct():
    num_hex = input("Ingrese un número hexadecimal: ")

    try:
        octal = oct(int(num_hex, 16))
        print("El número hexadecimal", num_hex, "convertido a octal es:", octal)
    except ValueError:
        print("Por favor, ingrese un número hexadecimal válido.")

def resta_octales():
    num1 = input("Ingrese el primer número octal: ")
    num2 = input("Ingrese el segundo número octal: ")

    try:
        resta = oct(int(num1, 8) - int(num2, 8))
        print("La resta de", num1, "y", num2, "es:", resta)
    except ValueError:
        print("Por favor, ingrese números octales válidos.")

def salir():
    print("Saliendo del programa.")

