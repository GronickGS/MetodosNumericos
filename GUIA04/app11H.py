import numpy as np
import matplotlib.pyplot as plt

def calcular_suma_vectorial(vectores):
    suma = np.zeros_like(vectores[0])
    for vector in vectores:
        suma += np.array(vector)
    return suma

def graficar_vectores(vectores, suma):
    fig, ax = plt.subplots()
    for vector in vectores:
        ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, label=f'Vector ({vector[0]}, {vector[1]})')
    ax.quiver(0, 0, suma[0], suma[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'Suma ({suma[0]}, {suma[1]})')
    ax.set_xlim(0, max(suma[0], 1) + 1)
    ax.set_ylim(0, max(suma[1], 1) + 1)
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_title('Suma Vectorial')
    ax.legend()
    plt.grid()
    plt.show()

def main():
    # Vectores definidos por defecto
    vectores = [[2, 3], [3, 1], [1, 4]]

    # Calcular la suma vectorial
    suma = calcular_suma_vectorial(vectores)
    print("La suma vectorial es:", suma)

    # Graficar los vectores y la suma
    graficar_vectores(vectores, suma)

if __name__ == "__main__":
    main()
