import sympy as sym
from sympy.abc import a,x

fsx = a * (x**2)

diff = sym.diff(fsx, x)
sym.pprint(diff)

sym.pprint(a * sym.diff(x**2, x))