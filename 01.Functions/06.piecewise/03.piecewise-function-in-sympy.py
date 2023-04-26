import sympy as sym
import matplotlib.pyplot as plt

x = sym.var('x')
f = sym.Piecewise(
    (0, x < 0), 
    (-2 * x, ((x >= 0) & (x < 3))), 
    (0.1 * (x**3), x >= 3)
)

sym.plot(f, (x, -3, 5),title='Piecewise function', xlabel='x')
plt.show()