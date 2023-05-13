import sympy as sym

sx = sym.var("x")
fsx = sym.cos(sx)

f1 = sym.diff(fsx, sx)
sym.pprint(f"$[\\cos(x)]' = {f1}$")

f2 = sym.diff(f1, sx)
sym.pprint(f"$[-\\sin(x)]' = {f2}$")

f3 = sym.diff(f2, sx)
sym.pprint(f"$[-\\cos(x)]' = {f3}$")

f4 = sym.diff(f3, sx)
sym.pprint(f"$[\\sin(x)]' = {f4}$")