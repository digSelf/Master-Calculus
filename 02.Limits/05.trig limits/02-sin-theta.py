import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# create the symbolic functions
sx = sym.var('x')
fsx = sym.sin(sx) / sx

gsx = -1/sx
hsx = 1/sx

sym.plot(
    gsx, fsx, hsx, 
    (sx, -100, 100), 
    xlim=(-100, 100), ylim=(-1, 1)
)

# plot in matplotlib
fx = sym.lambdify(sx, fsx, 'numpy')
gx = sym.lambdify(sx, gsx, 'numpy')
hx = sym.lambdify(sx, hsx, 'numpy')

x = np.linspace(-100, 100, 1000)

plt.plot(x, fx(x), label='f(x)')
plt.plot(x, gx(x), label=r'$-\frac{1}{x}$')
plt.plot(x, hx(x), label=r'$\frac{1}{x}$')

plt.xlim((-100, 100))
plt.ylim((-1, 1))

plt.grid()
plt.legend()
plt.show()

# plot the signs of the functions
plt.plot(x, np.sign(fx(x)), label='sign(f(x))')
plt.plot(x, np.sign(gx(x)), linewidth=3, label='sign(g(x))')
plt.plot(x, np.sign(hx(x)), linewidth=3, label='sign(h(x))')

plt.xlim((-100, 100))

plt.grid()
plt.legend()
plt.show()

# compute the limit in sympy
print(f"the limit as x approches infinity: {sym.limit(fsx, sx, sym.oo, dir='+-')}")