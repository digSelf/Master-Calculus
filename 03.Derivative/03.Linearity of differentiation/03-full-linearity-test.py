import sympy as sym

a, b, x = sym.symbols("a b x")

fsx = a * (x**2) + b * sym.cos(x)
sym.pprint(f"Derivative of the combined function: {sym.diff(fsx, x)}")

result = 0
for item in fsx.args:
    result += sym.diff(item, x)

sym.pprint(f"Combination of individual components: {result}")