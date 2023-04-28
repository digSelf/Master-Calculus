import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

coef = np.random.randint(low=1, high=100)

sx = sym.var("x")
fsx = coef * sym.exp(-sx) * sym.cos(2 * sym.pi * sx)

sym.pprint(fsx)

f = sym.lambdify(sx, fsx, 'numpy')
x = np.linspace(-3, 3)

plt.plot(x, f(x))
plt.grid()

plt.title(f"$f(x) = {sym.latex(fsx)}$")
plt.show()