import numpy as np
import matplotlib.pyplot as plt

fx = lambda x : np.cos(x * np.pi) + np.log(x) ** 2

exp_factor = 4
g = 1 + 1e-5 - np.linspace(1, 1e-4 ** exp_factor, 10) ** (1 / exp_factor)

left_xs = 3 - g
right_xs = 3 + g

x = np.linspace(1e-5, 2 * np.pi, 1000)
plt.plot(x, fx(x), 'k-', label='y = f(x)')

plt.plot(left_xs, fx(left_xs), 'o', markerfacecolor='w', label='from the left')
plt.plot(right_xs, fx(right_xs), 'o', markerfacecolor='w', label='from the right')

plt.xlim((2, 4))
plt.ylim((-1.5, 2 * np.pi))

plt.grid()
plt.legend()

plt.show()
