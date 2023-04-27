import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.sin(x)
g = lambda x : np.log(x)
h = lambda x : 2 * (x ** 2) + 5

x = np.linspace(-100 * np.pi, 100 * np.pi, 2000)

plt.plot(x, f(g(h(x))))
plt.show()