import random
from colorama import Fore, Style  # Importar colorama para cambiar el color del texto

# Definir la cantidad de números aleatorios
cantidad_numeros = int(input("X: "))

# Lista de colores disponibles
colores = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW]

while True: 
    # Generar una lista de números aleatorios
    numeros_aleatorios = [random.randint(0, 1) for _ in range(cantidad_numeros)]
    
    # Seleccionar un color aleatorio de la lista de colores
    color_aleatorio = random.choice(colores)
    
    # Imprimir la lista de números aleatorios en el color aleatorio
    print(color_aleatorio + ' '.join(map(str, numeros_aleatorios)))
    
    # Reiniciar el color a su valor por defecto
    print(Style.RESET_ALL)
