import sympy as sym
from sympy.abc import x

f = 3*(x**4) + sym.cos(x) + sym.exp(-(x**2))
df = sym.diff(f, x, 1)
ddf = sym.diff(f, x, 2)
dddf = sym.diff(f, x, 3)

print("The function is")
sym.pprint(f)

print("The 1-order derivative is")
sym.pprint(df)

print("The 2-order derivative is")
sym.pprint(ddf)

print("The 3-order derivative is")
sym.pprint(dddf)
