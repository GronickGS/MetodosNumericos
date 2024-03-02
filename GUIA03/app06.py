import math
import numpy as np
import matplotlib.pyplot as plt

def func_cos(x, n):
    cos_aprox = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2**i)
        cos_aprox += (coef) * (num/denom)
    return cos_aprox

angulos = np.arange(-2*np.pi, 2*np.pi,0.1)
p_cos = np.cos(angulos)
t_cos = [func_cos(angle, 3) for angle in angulos]
fig, ax = plt.subplots()
ax.plot(angulos, p_cos)
ax.plot(angulos, t_cos)
ax.set_ylim([-5,5])
ax.legend(['funcion cos()', 'serie de Taylor - 3 terminos'])

plt.show()
