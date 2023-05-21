import sympy as sym

sx = sym.var("x")

def newton_iter(f, df, x0):
    x1 = x0 - f.subs(sx, x0) / df.subs(sx, x0)
    return x1 

fsx = 2*(sx**3) - 3
dfsx = sym.diff(fsx, sx)

x0 = 1
x1 = newton_iter(fsx, dfsx, x0)
sym.pprint("first iteration: {}".format(x1))

x2 = newton_iter(fsx, dfsx, x1)
sym.pprint("second iteration: {}".format(x2))
