import sympy as sym

x, a, b = sym.symbols('x a b')

f1 = (x**a)**b
f2 = x**(a * b)

# use sym.powsimp instead sym.simplify
# why does the sympy not simplify the expression f1?
sym.pprint(sym.powsimp(f1))
sym.pprint(f2)

# substitute a = 3, b = 7
a1 = 3
b1 = 7
sym.pprint((x ** a1) ** b1)
sym.pprint(sym.simplify(sym.Subs(f1, (a, b), (a1, b1))))

# substitute x = -2, a = 4.1, b = -0.3
f3 = sym.Subs(f1, (x, a, b), (-2, 4.1, -.3))
f4 = sym.Subs(f2, (x, a, b), (-2, 4.1, -.3))
sym.pprint(f"f3: {f3.evalf()}")
sym.pprint(f"f4: {f4.evalf()}") # we found that f3 not equals to f4

# control group where base number assigns to positive value.
f5 = sym.Subs(f1, (x, a, b), (2, 4.1, -.3))
f6 = sym.Subs(f2, (x, a, b), (2, 4.1, -.3))
sym.pprint(f"f5: {f5}, value = {f5.evalf()}")
sym.pprint(f"f6: {f6}, value = {f6.evalf()}") 

f7 = sym.Subs(f1, (x, a, b), (-2, 4.1, .3))
f8 = sym.Subs(f2, (x, a, b), (-2, 4.1, .3))
sym.pprint(f"f7: {f7}, value = {f7.evalf()}")
sym.pprint(f"f8: {f8}, value = {f8.evalf()}") 

# add constraint
y, c, d = sym.symbols("y c d", positive=True)
f9 = (y**c)**d
# sym.pprint(sym.simplify(f9))
sym.pprint(sym.powsimp(f9))
