import sympy as sym
from sympy.abc import x
import numpy as np

fx = 2 * (x**2) - 3 * x + 1
a = -1
c = 2

def solveMVT(fx, a, c):
    global_average_slope = (fx.subs(x, c) - fx.subs(x, a)) / (c - a)
    dfx = sym.diff(fx, x)
    roots = sym.solve(sym.Eq(dfx, global_average_slope), x)
    
    # verify the validation of the solutions
    roots = np.array(roots).astype(np.float64)
    return roots[np.bitwise_and(a < roots, roots < c)]

result = solveMVT(fx, a, c)
print(result)