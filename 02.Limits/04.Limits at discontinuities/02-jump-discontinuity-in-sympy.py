import sympy as sym
# from sympy.abc import x

sx = sym.var('x')
fsx = sym.Piecewise(
    (sym.sin(sx * sym.pi), sx < 0),
    (1.5, sym.Eq(sx, 0)),
    (-(sx-2)**2, sx > 0)
)
sym.pprint(fsx)

# sym.plot(fsx, ylim=(-2, 2))

# There are several errors in sympy to calculate limit
# and I do not know why. 
# That gives me a hint: do not blindly trust sympy.
# compute the limit from the left
print(f"the limit from the left: {sym.limit(fsx, sx, 0, dir='-')}")

# compute the limit from the right
print(f"the limit from the left: {sym.limit(fsx, sx, 1, dir='+')}")

# compute the two-sided limt
print(f"the two-sided limit: {sym.limit(fsx, sx, 0, dir='+-')}")

# compute the function value at the point 0
print(f"the function value: {fsx.subs(sx, 0) : .2f}")
