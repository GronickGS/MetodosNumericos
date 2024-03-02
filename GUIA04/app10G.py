import matplotlib.pyplot as plt
# Definición del punto de inicio del vector
x_start, y_start = 0, 0
# Componentes del vector
x_component, y_component = 3, 4
# Creación de la figura y los ejes
fig, ax = plt.subplots()
# Trazado del vector utilizando la función quiver
ax.quiver(x_start, y_start, x_component, y_component, angles='xy', scale_units='xy', scale=1, color='b', label='vector')
# Establecimiento de los límites de los ejes
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
# Etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
# Título del gráfico
ax.set_title('Gráfico de un Vector')
# Leyenda para el vector trazado
ax.legend()
# Malla en el gráfico
plt.grid()
# Línea horizontal en y = 0
plt.axhline(0, color='black', linewidth=0.5)
# Línea vertical en x = 0
plt.axvline(0, color='black', linewidth=0.5)
# Mostrar el gráfico
plt.show()
