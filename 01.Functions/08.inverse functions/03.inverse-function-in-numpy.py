import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.log(2 * x)
g = lambda x : np.exp(x) / 2

x = np.linspace(1e-5, 5)

plt.plot(x, f(x), label='f(x)')
plt.plot(x, g(x), label='g(x)')
plt.plot(x, f(g(x)), label='f(g(x))')
plt.plot(x, g(f(x)), '.', label='g(f(x))')

plt.ylim((-1, 10))
plt.legend()

plt.show()