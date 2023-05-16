import sympy as sym
from sympy.abc import x, y, z
# from sympy.geometry import util 

target = x * y - 1
dy = sym.idiff(target, y, x)

sym.pprint(dy)

sym.plot_implicit(target)
# sym.plot_implicit(sym.Eq(dy, 0))  # ?

explicit = sym.solve(sym.Eq(target, 0), y)[0]
sym.pprint(explicit)

new_dy = dy.subs(y, explicit)
sym.pprint(new_dy)
sym.plot_implicit(sym.Eq(new_dy, z))