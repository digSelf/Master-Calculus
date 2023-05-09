import sympy as sym

x = sym.var("x")

fsx = sym.sin(x) / x
gsx = (sym.cos(x) - 1) / x

print(f"the limit of sin(x)/x as x-> 0: {sym.limit(fsx, x, 0, dir='+-')}")
print(f"the limit (cos(x) - 1)/x as x->0: {sym.limit(gsx, x, 0, dir='+-')}")
