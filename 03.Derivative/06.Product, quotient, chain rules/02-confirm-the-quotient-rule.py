import sympy as sym
from sympy.abc import x

f = x**2
g = sym.cos(x)

f_over_g = f / g

sym.pprint(f"f/g: {sym.diff(f_over_g, x)}")

expr = (sym.diff(f, x) * g - f * sym.diff(g, x)) / g**2
sym.pprint(f"(f'g - fg')/g^2: {expr}")
