import numpy as np
import matplotlib.pyplot as plt

f = lambda x : (np.cos(x ** 2) ** 2) + np.pi

x = np.linspace(-2.1, 2.1, 1000)

plt.title(r'$f(x) = \cos^2(x^2) + \pi$')

plt.plot(x, f(x))
plt.grid()
plt.show()