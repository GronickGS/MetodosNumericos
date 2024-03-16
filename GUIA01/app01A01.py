'''
A. Para convertir un numero decimal a binario se debe ir dividiendo el número decimal
entre dos y anotar en una columna a la derecha el resto. La lista de ceros y unos leídos
de abajo a arriba es el resultado.

'''

# Definición de la función DecimalABinario que convierte un número decimal a binario
def DecimalABinario(num):
    # Comprueba si el número dado es mayor o igual a 1
    if num >= 1:
        # Llama recursivamente a la función con el cociente entero de num dividido por 2
        DecimalABinario(num // 2)
        # Imprime el residuo de la división de num por 2, que es el bit actual de la representación binaria
        print(num % 2)

# Bucle principal que continuará ejecutándose hasta que se ingrese 'x'
while True:
    # Solicita al usuario que ingrese un número decimal
    num = input("Ingrese decimal: ") 
    # Verifica si la entrada del usuario es 'x', en cuyo caso se rompe el bucle
    if num == 'x': 
        break
    else: 
        # Llama a la función DecimalABinario con el número decimal ingresado convertido a entero
        DecimalABinario(int(num))
