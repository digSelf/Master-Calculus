import numpy as np
import matplotlib.pyplot as plt

# The three following statements could be replaced by the for-loop.
x1 = np.linspace(0, 2*np.pi, 100)
x2 = np.linspace(0, 2*np.pi, 1000)
x3 = np.linspace(0, 2*np.pi, 10000)

f = [0] * 3
f[0] = x1, np.tan(x1), '100 points'
f[1] = x2, np.tan(x2), '1000 points'
f[2] = x3, np.tan(x3), '10000 points'

for x, func, label in f:
    plt.plot(x, func, label=label)

plt.legend()
plt.grid()
plt.show()
