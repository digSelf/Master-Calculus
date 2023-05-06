from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

fx = lambda x : (np.cos(x ** 2) ** 2) + np.pi

a = 1

# starting x-axis values
x0 = np.array([a - 1, a + 1])

# initialize ...
iter_bound = 10
limit_values = np.zeros((iter_bound, 2))
x_axis_values = np.zeros((iter_bound, 2))

# zeno's paradox algorithm
for i in range(iter_bound):
    # compute and store x0, y = f(x0)
    x_axis_values[i, :] = x0
    limit_values[i, :] = fx(x0)

    # update x-values
    x0 = (x0 + a) / 2

# print out the results 
# left_side_results = np.vstack((x_axis_values[:, 0], limit_values[:, 0])).T  # transpose
# pprint(left_side_results)

domain = np.linspace(-2.1, 2.1, 500)
plt.plot(domain, fx(domain), color='black', label='y = f(x)')

plt.plot(x_axis_values[:, 0], limit_values[:, 0], 'o', markerfacecolor='w', label='from left')
plt.plot(x_axis_values[:, 1], limit_values[:, 1], 'o', markerfacecolor='w', label='from right')

plt.legend()
plt.grid()
plt.show()

