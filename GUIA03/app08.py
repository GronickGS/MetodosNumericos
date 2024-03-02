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

fig, ax = plt.subplots()
ax.plot(angulos, p_cos)

for  i in range(1,6):
    t_cos = [func_cos(angulo, i) for angulo in angulos]
    ax.plot(angulos, t_cos)

ax.set_ylim([-7,4])

legend_lst = ['funcion cos()']
for i in range(1,6):
    legend_lst.append(f'Series de Taylor - [i] terminos')

ax.legend(legend_lst, loc=3)

plt.show()
