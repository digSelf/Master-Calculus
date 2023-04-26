import numpy as np
import sympy as sym

# in numpy
# The domain is [-3, 5]
x = np.linspace(-3, 5, 1000)

# The pieces
f1 = 0 * x * (x < 0)
f2 = -2 * x * ((x >= 0) & (x < 3))
f3 = 0.1 * (x ** 3) * (x >= 3)

# The function composited by the above pieces
f = f1 + f2 + f3
idx = np.argmin(np.abs(x - .5))
print(f"(numpy): at x = {x[idx]: .5f}, f(x) = {f[idx]: .5f}")

# in sympy
sx = sym.var('x')
sf = sym.Piecewise((0, sx < 0), (-2*sx, ((sx >= 0) & (sx < 3))), (0.1*(sx**3), sx >= 3))

# print(f"(sympy): at x = 0.5, f(x) = {sym.Subs(sf, sx, .5).evalf() : .5f}")
print(f"(sympy): at x = 0.5, f(x) = {sf.subs(sx, .5) : .5f}")
