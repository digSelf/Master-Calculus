import sympy as sym

# The real parameter will ignore the complex roots if it is true.
sx = sym.var("sx", real=True)
fsx = 2 * (sx**3) - 3

roots = sym.solve(fsx, sx)
sym.pprint(roots)

# The function sym.N converse a symbolic result to a numpy result
numerical = sym.N(roots[0])
print(numerical)
