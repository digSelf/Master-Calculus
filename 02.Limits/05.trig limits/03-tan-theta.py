import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

sx = sym.Symbol('x')
fsx = sym.tan(sx) / sx
gsx = sym.sin(sx) / sx
hsx = 1 / sym.cos(sx)

fx = sym.lambdify(sx, fsx, 'numpy')
gx = sym.lambdify(sx, gsx, 'numpy')
hx = sym.lambdify(sx, hsx, 'numpy')

x = np.linspace(-np.pi, np.pi, 1000)
plt.plot(x, fx(x), label=r'$f_0$')
plt.plot(x, gx(x), label=r'$f_1$')
plt.plot(x, hx(x), label=r'$f_2$')

plt.plot(x[::20], (fx(x) * gx(x))[::20], 'o', label=r'f_1 \cdot f_2')

plt.xlim((-np.pi, np.pi))
plt.ylim((-20, 20))

plt.grid()
plt.legend()
plt.show()

# compute the function value at 0
print(f"the function value at 0: {fsx.subs(sx, 0)}")

# compute the limits
sym.pprint(f"the limit as $\\theta\\to 0$: {sym.limit(fsx, sx, 0, dir='+-')}")
