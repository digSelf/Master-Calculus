import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# in numpy
x = np.linspace(-1, 2, 1000)
fx = np.sin(1 / (x - 1))

plt.plot(x, fx)
plt.show()

# in sympy
sx = sym.var('x')
fsx = sym.sin(1 / (x - 1))

sym.plot(fsx, (sx, -1, 2))