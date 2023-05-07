import sympy as sym
from sympy.abc import x 

fx = sym.Abs(x - 2) / (x - 2)

# plot the function
sym.plot(fx, (x, -2, 4))

# compute the limit
left_limit = sym.limit(fx, x, 2, dir='-')
sym.pprint(f'The limit from the left: {left_limit}')

right_limit = sym.limit(fx, x, 2, dir='+')
sym.pprint(f"The limit from the right: {right_limit}")

# error: the limit does not exist.
# limit = sym.limit(fx, x, 2, dir="+-")
# sym.pprint(f"The limit from the two-sided: {limit}")