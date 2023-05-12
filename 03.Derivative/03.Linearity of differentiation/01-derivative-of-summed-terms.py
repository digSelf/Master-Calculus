import sympy as sym

a, b, c, x = sym.symbols("a b c x")

ax = a * (x**2) 
bx = b * (x**3)  
cx = c * sym.exp(2 * x)
fsx = ax + bx + cx 

# or use fsx.args to get each piece in fsx
dfx = sym.diff(fsx, x)
print("Derivative of combined function: ")
sym.pprint(dfx)

print("Derivative of ax^2: ")
dax = sym.diff(ax, x)
sym.pprint(dax)

print("Derivative of bx^3: ")
dbx = sym.diff(bx, x)
sym.pprint(dbx)

print("Derivative of ce^2x: ")
dcx = sym.diff(cx, x)
sym.pprint(dcx)

print("Combination of individual components: ")
t = dax + dbx + dcx
sym.pprint(t)