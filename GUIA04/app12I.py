import matplotlib.pyplot as plt
# Definición de las fuerzas
F1 = [4, 0]  # (4N, 0N) hacia la derecha
F2 = [0, 3]  # (0N, 3N) hacia arriba
F3 = [-3, -4]  # (-3N, -4N) hacia abajo y hacia la izquierda
# Cálculo de la fuerza resultante sumando las tres fuerzas
F_resultante = [F1[0] + F2[0] + F3[0], F1[1] + F2[1] + F3[1]]
# Graficación de las fuerzas
plt.figure(figsize=(8, 6))
# Graficar F1
plt.quiver(0, 0, F1[0], F1[1], angles='xy', scale_units='xy', scale=1, color='r', label='F1 (4N, 0N)')
# Graficar F2
plt.quiver(0, 0, F2[0], F2[1], angles='xy', scale_units='xy', scale=1, color='g', label='F2 (0N, 3N)')
# Graficar F3
plt.quiver(0, 0, F3[0], F3[1], angles='xy', scale_units='xy', scale=1, color='b', label='F3 (-3N, -4N)')
# Graficar la fuerza resultante
plt.quiver(0, 0, F_resultante[0], F_resultante[1], angles='xy', scale_units='xy', scale=1, color='purple', label='F Resultante')
# Configuración de los ejes
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Fuerzas y Fuerza Resultante')
plt.grid()
plt.legend()
plt.show()
