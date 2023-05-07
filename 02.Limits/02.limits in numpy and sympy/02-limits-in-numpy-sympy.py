import numpy as np
import sympy as sym

# create a symbolic variable
sx = sym.var("x")
fsx = sym.cos(sx * sym.pi) + sym.ln(sx) ** 2

# limit as x approaches 3 from the left
left_limit = sym.limit(fsx, sx, 3, dir='-')
sym.pprint(f"Limit as x approaches 3 from the left: {left_limit}")

# limit as x approaches 3 from the right
# default is from the right.
right_limit = sym.limit(fsx, sx, 3, dir='+')
sym.pprint(f"Limit as x approaches 3 from the right: {right_limit}")

# compute the two-sided limit
limit = sym.limit(fsx, sx, 3, dir='+-')
sym.pprint(f"Function value at limit (sympy): {limit}")

# function value in numpy
# sym.N == evaluate in numpy 
value = sym.N(limit)
sym.pprint(f"Function value at limit (numpy): {value}")