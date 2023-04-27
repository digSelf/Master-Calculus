import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 2000)

f = lambda x : 2 * (x ** 2) - 4 
g = lambda x : 7 * np.abs(x) + 3

plt.plot(x, f(x), label='$f(x)$')
plt.plot(x, g(x), label='$g(x)$')
plt.plot(x, f(g(x)), label='$f(g(x))$')
plt.plot(x[::10], g(f(x))[::10], '.', label='$g(f(x))$')

plt.xlim((-4, 4))
plt.ylim((-10, 50))

plt.grid()
plt.legend()
plt.show()
