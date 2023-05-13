import sympy as sym

sx = sym.var("x")
fsx = sym.acos(sx)

for i in range(4):
    dfsx = sym.diff(fsx, sx)
    sym.pprint(f"[{fsx}]' = {dfsx}")
    fsx = dfsx