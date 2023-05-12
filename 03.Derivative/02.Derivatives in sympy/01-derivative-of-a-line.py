import sympy as sym
import matplotlib.pyplot as plt

sx = sym.Symbol("x")
fsx = 5/4 * sx + 9 / 4
sym.pprint(fsx)

sym.plot(fsx, (sx, -1, 6), axis_center=[0, 0])

sym.pprint(sym.diff(fsx, sx))