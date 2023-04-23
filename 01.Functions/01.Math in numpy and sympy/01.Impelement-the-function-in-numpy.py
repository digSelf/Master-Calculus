import numpy as np
import matplotlib.pyplot as plt

# change the font in the figure to times new roman
plt.rc('font',family='Times New Roman')

# The function: y = f(x) = x^2 + 3x^3 - x^4
# define domain
domain = [-2, 2]
x = np.linspace(domain[0], domain[-1])  # sampling

# define the function
# f = lambda x: x ** 2 + 3 * x ** 3 - x ** 4
# y = [f(v) for v in x]
y = x ** 2 + 3 * x ** 3 - x ** 4

# plot figure
plt.plot(x, y, label='$y = x^2 + 3x^3 - x^4$')

plt.grid()
plt.legend()

# change x limit
plt.xlim(domain[0], domain[-1])

plt.xlabel('x')
plt.ylabel('y = f(x)')

plt.show()