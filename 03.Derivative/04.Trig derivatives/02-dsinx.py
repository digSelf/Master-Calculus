import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
x = np.arange(-1.5 * np.pi, 1.5 * np.pi, step=dx)

fx = np.sin(x)
dfx = np.diff(fx) / dx

plt.plot(x, fx, label=r'$\sin(x)$')
plt.plot(x[:-1], dfx, label=r'$diff(\sin(x))$')
plt.plot(x[::10], np.cos(x)[::10], '.', label=r'$\cos(x)$')

plt.xlim((-1.5*np.pi, 1.5*np.pi))
plt.legend()
plt.show()
