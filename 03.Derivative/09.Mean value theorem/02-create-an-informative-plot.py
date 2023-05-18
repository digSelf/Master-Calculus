import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 4)
fx = lambda x : 2 * x**2 - 3 * x + 1

a = -1 
c = 2

plt.plot(x, fx(x), label='f(x)')
# plt.scatter((a, 2), (fx(a), fx(2)))
plt.scatter(a, fx(a), marker='.', label='a')
plt.scatter(c, fx(c), marker='.',  label='c')

# x = a, x = 2
plt.axvline(x=a, ls=':', c='r', label='x = a')
plt.axvline(x=c, ls=':', c='c', label='x = c')

# secant line
plt.plot((a, c), (fx(a), fx(c)), ls=":", label='secant')

# tangent line
r = 1/2
k = (fx(c) - fx(a)) / (c - a)
b = fx(r)
gx = lambda x, k, b : k * x + b
plt.scatter(r, fx(r), marker=".", color='k', label='b')

# subrange
sx = np.linspace(a, c)
plt.plot(sx, gx(sx, k, b), ls=':', c='k', label='tagent')

plt.ylim((-2, 30))
plt.legend()
plt.show()