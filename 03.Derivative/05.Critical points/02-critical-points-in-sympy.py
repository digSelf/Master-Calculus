import sympy as sym

sx = sym.var("x")
fsx = sx ** 2 + sx ** 3

dfsx = sym.diff(fsx, sx)
sym.pprint(dfsx)

points = sym.solve(sym.Eq(dfsx, 0), sx)
for pt in points:
    print(f"Critical point/value: ({pt}, {fsx.subs(sx, pt)})")
