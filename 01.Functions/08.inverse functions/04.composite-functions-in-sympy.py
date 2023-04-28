import sympy as sym

# create symbolic variable
sx = sym.var('x')

# construct the expression with the variable sx
fsx = sym.sin(sx)
gsx = sym.ln(sx)
hsx = 2 * (sx ** 2) + 5

# substitute the variable sx to hsx and gsx, respectively.
# alternatively, expr = fsx.subs(sx, gsx.subs({'x' : hsx}))
expr = fsx.subs(sx, gsx.subs(sx, hsx))
sym.pprint(expr)

sym.plot(expr, (sx, -100, 100), ylabel=None, xlabel='x', 
         title=r'$y = \sin(\ln(2x^2 + 5)))$')