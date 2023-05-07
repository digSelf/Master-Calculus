import sympy as sym
from sympy.abc import x

fsx = sym.ln(x) + x ** 2
gsx = sym.exp(-x) + x ** 3
hsx = x**3 + x**2 + x

# verify the first group
eq1 = sym.limit(fsx / gsx, x, sym.pi, dir='+-') \
    - sym.limit(fsx, x, sym.pi, dir='+-') \
        / sym.limit(gsx, x, sym.pi, dir='+-')
if eq1 < 1e-5:
    print("the expressions in the first group are the same")

# verify the second group
left_side = sym.limit(gsx / hsx, x, 0, dir='+-')
sym.pprint(left_side)
right_side = sym.limit(gsx, x, 0, dir='+-') / sym.limit(hsx, x, 0, dir='+-')
sym.pprint(right_side)

# the four properties both have a proposition:
# i.e., the limit of the each part must exist.
sym.pprint(left_side - right_side)
