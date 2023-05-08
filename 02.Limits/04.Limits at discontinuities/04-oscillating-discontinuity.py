import sympy as sym

x = sym.var('x')
fsx = sym.sin(x**(-1))

# sym.plot(fsx)
print(f"the limit as x->0 from the left: {sym.limit(fsx, x, 0, dir='-')}")
print(f"the limt as x->0 from the right: {sym.limit(fsx, x, 0, dir='+')}")
print(f"the two-sided limit as x->0: {sym.limit(fsx, x, 0, dir='+-')}")