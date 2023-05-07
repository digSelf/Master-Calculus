import sympy as sym

sx = sym.var("x")
fsx = sym.ln(sx) + sx**2
gsx = sym.exp(-sx) + sx**3

eq = sym.limit(fsx * gsx, sx, sym.pi, dir='+-') \
    - sym.limit(fsx, sx, sym.pi, dir='+-') \
        * sym.limit(gsx, sx, sym.pi, dir='+-')

if eq < 1e-5:
    print("the expressions are the same.")
