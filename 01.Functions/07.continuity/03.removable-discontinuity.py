import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(-2, 2, 100)
x = np.arange(-2, 2, .1)

f1 = np.sin(np.pi * x) + x ** 2
f2 = (np.pi - x**2) * (np.abs(x) < 1e-5)

# fx = f1
# fx[np.argmin(np.abs(x))] = np.pi
fx = f1 + f2

plt.scatter(x, fx)
plt.show()