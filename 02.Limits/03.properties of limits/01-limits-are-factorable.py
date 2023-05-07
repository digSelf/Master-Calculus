import sympy as sym
import numpy as np

sx = sym.var('x')
fsx = sx ** 3 / 3 + 100 * sym.sqrt(sym.Abs(sx))

verification_times = 100
for i in range(verification_times):
    c = np.random.randint(-100, 100)
    eq = sym.limit(c * fsx, sx, 5, dir='+-') - c * sym.limit(fsx, sx, 5, dir='+-')
    if eq > 1e-5:
        print("the limits are not equal")
        break