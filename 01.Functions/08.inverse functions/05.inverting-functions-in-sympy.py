import sympy as sym

sx = sym.var('x')
sy = sym.var('y')

fsx = 2 * sx + 3
gsx = 2 * sx + sym.sin(sx)

# 1.get the inverse.
# sy - fsx = 0
# because sympy assume that we are set the equation to 0.
# we can drop off '= 0' 
solved_result = sym.solve(sy - fsx, sx)
inv_fsx = solved_result[0].subs(sy, sx)

# there is no inverse for the function g(x)
# it is invertible.
# inv_gsx = sym.solve(sy - gsx, sx)
sym.pprint(inv_fsx)

# 2. demonstrate
lhs = inv_fsx.subs(sx, fsx.subs(sx, 4))
rhs = fsx.subs(sx, inv_fsx.subs(sx, 4))
result = sym.Eq(lhs, rhs)

print(result)
print(f"lhs: {lhs}, rhs: {rhs}")
