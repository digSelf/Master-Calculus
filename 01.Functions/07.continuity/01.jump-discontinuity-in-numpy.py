import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 2)

funcs = [0] * 3

funcs[0] = x[x < 0], np.sin(x[x < 0] * np.pi) 
funcs[1] = 0, 1.5
funcs[2] = x[x > 0], -(x[x > 0] - 2) ** 2

marker = '-o-'
for i, value in enumerate(funcs):
    xx, f = value
    plt.plot(xx, f, marker[i])

plt.xlim((-1, 2))
plt.ylim((-4, 2))
plt.show()