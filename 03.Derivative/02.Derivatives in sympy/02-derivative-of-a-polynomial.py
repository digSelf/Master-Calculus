import sympy as sym
from sympy.abc import x

fx = x**2
sym.plot(fx, axis_cetner=[0, 0])

sym.pprint(sym.diff(fx, x))