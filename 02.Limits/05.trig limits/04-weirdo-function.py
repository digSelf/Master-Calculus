import sympy as sym
from sympy.calculus.util import continuous_domain

sx = sym.var('x')

fsx = sx**2 * sym.exp(-sx**2) * sym.ln(sx**2) * sym.sin(sx)
# sym.pprint(fsx)

print(f"the function value at x = 0: {fsx.subs(sx, 0)}")
print(f"the limit as x approaches 0: {fsx.limit(sx, 0, dir='+-')}")

print("the domain is: ")
sym.pprint(continuous_domain(fsx, sx, sym.S.Reals))

# compute the limit of each part as x -> 0
print(f"the limit of x^2: {sym.limit(sx**2, sx, 0, dir='+-')}")
print(f"the limit of exp(-x^2): {sym.limit(sym.exp(-sx**2), sx, 0, dir='+-')}")
print(f"the limit of ln(x^2): {sym.limit(sym.ln(sx**2), sx, 0, dir='+-')}")
print(f"the limit of sin(x): {sym.limit(sym.sin(sx), sx, 0, dir='+-')}")

# compute the product of the limit
result = sym.limit(sx**2, sx, 0, dir='+-') \
    * sym.limit(sym.exp(-sx**2), sx, 0, dir='+-') \
    * sym.limit(sym.ln(sx**2), sx, 0, dir='+-') \
    * sym.limit(sym.sin(sx), sx, 0, dir='+-')
print(f"the limit of the product: {result}")