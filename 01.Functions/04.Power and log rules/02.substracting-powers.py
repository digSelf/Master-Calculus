import sympy as sym

x, a, b = sym.symbols("x a b")

f1 = x**a / x**b
sym.pprint(f1)
sym.pprint(sym.simplify(f1))

f2 = x**(a - b)
sym.pprint(f2)

a1 = b1 = 4
result = sym.Subs(f1, (a, b), (a1, b1))
sym.pprint(sym.simplify(result))

# 0^0 could be Nan(not a nubmer), or 0^0 = 1
# it depends on what you need.
# print(0**0)