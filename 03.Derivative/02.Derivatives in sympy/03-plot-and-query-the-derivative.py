import sympy as sym
from sympy.abc import x


fx = x**2
sym.plot(fx, axis_cetner=[0, 0])

dfx = sym.diff(fx, x)
sym.plot(dfx)

values = [-1, 0, 2]
for v in values:
    print(f"the derivative of {v} = {dfx.subs(x, v)}")
