import sympy as sym

sx = sym.Symbol('x')
fsx = sym.Piecewise(
    (sx**2, sx < 1), 
    (-(sx**2)/2, sx >= 1)
)

# sym.pprint(fsx)
sym.plot(fsx, xlim=(-1, 3), ylim=(-2, 2))

dfsx = sym.diff(fsx, sx)
# sym.pprint(dfsx)
sym.plot(dfsx, xlim=(-1, 3), ylim=(-2, 2))

result = sym.solve(sym.Eq(dfsx, 0), sx)

# there is a bug in sympy to calculate the limit of the discontinuity point in a piecewise function.
left_limit = sym.limit(dfsx.args, sx, 1, dir='-')
right_limit = sym.limit(dfsx.args, sx, 1, dir='+')
if left_limit != right_limit:
    result.append(1)

for x in result:
    print(f"Critical point/value: ({x}, {fsx.subs(sx, x)})")