import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
fx = lambda x : 3 * x**2 - 3 * x + 4
dfx = lambda x : 6 * x - 3 

x = np.arange(-2, 2, step=dx)

plt.plot(x, fx(x), label='f(x)')
plt.plot(x, dfx(x), label='df(x)')

plt.grid()
plt.legend()
plt.show()
