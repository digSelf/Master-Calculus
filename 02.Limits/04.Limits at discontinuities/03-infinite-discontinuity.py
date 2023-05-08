import sympy as sym
from sympy.abc import x

fsx = 3 / (1 - x**2)
# sym.pprint(fsx)

sym.plot(fsx, xlim=(-2, 2), ylim=(-10, 10))

print(f"the limit as x->-1 from the left: {sym.limit(fsx, x, -1, dir='-')}")
print(f"the limit as x->-1 from the right: {sym.limit(fsx, x, -1, dir='+')}")
print(f"the two-sided limit as x->-1: {sym.limit(fsx, x, -1, dir='+-')}")
