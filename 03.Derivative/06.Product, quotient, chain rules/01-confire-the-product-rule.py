import sympy as sym
from sympy.abc import x

fx = x**2
gx = sym.cos(x)

product_diff = sym.diff(fx * gx, x)
diff_separate = sym.diff(fx, x) * gx + fx * sym.diff(gx, x)

sym.pprint(f"(fg)': {product_diff}")
sym.pprint(f"f'g + fg': {diff_separate}")
