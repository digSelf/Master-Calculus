import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, 2*np.pi, 1000)

# it outputs f = [0, 0, 0]
f = [0] * 3

# f[i] is a tuple of (function, label)
#       functions           label
f[0] = np.sin(np.cos(x)), r'$\sin\cos\theta$'
f[1] = np.cos(np.sin(x)), r'$\cos\sin\theta$'
f[2] = np.cos(x),         r'$\cos\theta$'

for func, label in f:
    plt.plot(x, func, label=label)

plt.legend()
plt.show()