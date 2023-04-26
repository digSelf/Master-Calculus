import matplotlib.pyplot as plt
import sympy as sym

x = sym.var('x')
expr = sym.Piecewise(
    (sym.sin(x * sym.pi), x < 0),
    (1.5, sym.Eq(x, 0)),  # cannot write 'x == 0'
    (-(x - 2)**2, x > 0)
)

# sym.pprint(expr)
sym.plot(expr, (x, -1, 2))
