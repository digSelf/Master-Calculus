import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
x = np.arange(-1.5 * np.pi, 1.5 * np.pi + 0.1, step=dx)
diff = np.diff(np.cos(x)) / dx

plt.plot(x, np.cos(x), label=r'$\cos(x)$')
plt.plot(x[:-1], diff, label=r'$diff(\cos(x))$')
plt.plot(x[::10], -np.sin(x)[::10], '.', label=r'$-\sin(x)$')

plt.xlim((-1.5*np.pi, 1.5*np.pi))

plt.legend()
plt.show()