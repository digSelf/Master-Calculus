import sympy as sym

# create three symoblic variables
x = sym.var('x')
a = sym.var('a')
b = sym.var('b')

# create the function: f = x^ax^b
# and simplify
f1 = sym.simplify(x**a * x**b)

# substitute for specific numbers
a1 = 3.4
b1 = 5.6

g = sym.Subs(f1, (a, b), (a1, b1))
sym.pprint(sym.simplify(g))

z = sym.Subs(x**a, a, a1) * sym.Subs(x**b, b, b1)
sym.pprint(sym.simplify(z))
