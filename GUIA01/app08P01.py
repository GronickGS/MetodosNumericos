# Función para mostrar el menú de opciones
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    # Itera sobre las claves del diccionario de opciones y las imprime ordenadas
    for clave in sorted(opciones):
        # Imprime la clave y la descripción de la opción
        print(f'{clave}: {opciones[clave][0]}')

# Función para leer la opción seleccionada por el usuario
def leer_opcion(opciones):
    while True:
        opcion = input('Opción: ')
        # Verifica si la opción ingresada está presente en el diccionario de opciones
        if opcion in opciones:
            return opcion
        else:
            print('Opción incorrecta, vuelva a intentarlo.')

# Función para ejecutar la opción seleccionada por el usuario
def ejecutar_opcion(opcion, opciones):
    # Ejecuta la función asociada con la opción seleccionada
    opciones[opcion][1]()

# Función para generar el menú principal y manejar la selección de opciones
def generar_menu(opciones, opcion_salida):
    opcion = None
    # Continúa mostrando el menú y ejecutando las opciones seleccionadas hasta que se seleccione la opción de salida
    while opcion != opcion_salida:
        mostrar_menu(opciones)  # Muestra el menú de opciones
        opcion = leer_opcion(opciones)  # Lee la opción seleccionada por el usuario
        ejecutar_opcion(opcion, opciones)  # Ejecuta la opción seleccionada
        print()  # Imprime una línea en blanco después de cada opción

# Función principal que define el menú principal y llama a generar_menu para iniciar el programa
def menu_principal():
    opciones = {
        '1': ("Suma de dos números binarios enteros", suma_binarios),
        '2': ("Multiplicación de dos números hexadecimales", multiplicacion_hex),
        '3': ("Conversión de Hexadecimal a Octal", conversion_hex_oct),
        '4': ("Resta de dos números octales", resta_octales),
        '5': ("Salir", salir),
    }
    generar_menu(opciones, '5')  # Genera el menú con las opciones y la opción de salida

# Función para realizar la suma de dos números binarios
def suma_binarios():
    num1 = input("Ingrese el primer número binario: ")
    num2 = input("Ingrese el segundo número binario: ")

    try:
        # Convierte los números binarios a enteros, suma y luego convierte el resultado de nuevo a binario
        suma = bin(int(num1, 2) + int(num2, 2))
        print("La suma de", num1, "y", num2, "es:", suma)
    except ValueError:
        print("Por favor, ingrese números binarios válidos.")

# Función para realizar la multiplicación de dos números hexadecimales
def multiplicacion_hex():
    num1 = input("Ingrese el primer número hexadecimal: ")
    num2 = input("Ingrese el segundo número hexadecimal: ")

    try:
        # Convierte los números hexadecimales a enteros, multiplica y luego convierte el resultado de nuevo a hexadecimal
        producto = hex(int(num1, 16) * int(num2, 16))
        print("El producto de", num1, "y", num2, "es:", producto)
    except ValueError:
        print("Por favor, ingrese números hexadecimales válidos.")

# Función para realizar la conversión de un número hexadecimal a octal
def conversion_hex_oct():
    num_hex = input("Ingrese un número hexadecimal: ")

    try:
        # Convierte el número hexadecimal a entero y luego a octal
        octal = oct(int(num_hex, 16))
        print("El número hexadecimal", num_hex, "convertido a octal es:", octal)
    except ValueError:
        print("Por favor, ingrese un número hexadecimal válido.")

# Función para realizar la resta de dos números octales
def resta_octales():
    num1 = input("Ingrese el primer número octal: ")
    num2 = input("Ingrese el segundo número octal: ")

    try:
        # Convierte los números octales a enteros, resta y luego convierte el resultado de nuevo a octal
        resta = oct(int(num1, 8) - int(num2, 8))
        print("La resta de", num1, "y", num2, "es:", resta)
    except ValueError:
        print("Por favor, ingrese números octales válidos.")

# Función para salir del programa
def salir():
    print("Saliendo del programa.")

# Llamada a la función principal para iniciar el programa
menu_principal()
