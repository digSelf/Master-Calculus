import numpy as np
import matplotlib.pyplot as plt

# define the piecewise function
def f(x):
    err = 1e-4
    y = np.zeros(x.shape)
    y[x < -err] = np.sin(x[x < -err] * np.pi)
    y[np.abs(x) < err] = 1.5
    y[x > err] = -(x[x > err] - 2) ** 2
    
    return y
    
# plot the function
domain = np.linspace(-1, 2, 1000)
values = f(domain)

plt.plot(domain, values, 'o', markersize=1)
plt.show()

# esitimate the limit
# exp_factor = 4
# delta = 1 + 1e-5 - np.linspace(1, 1e-4 ** exp_factor, 20) ** (1 / exp_factor)

# another method is using logspace
delta = np.logspace(np.log10(.1), np.log(.001), 100)

# from the left
left_xs = 0 - delta
left_ys = f(left_xs)

# from the right
right_xs = 0 + delta
right_ys = f(right_xs)

plt.plot(left_xs, left_ys, 'o', label='from the left')
plt.plot(right_xs, right_ys, 'o', label='from the right')
plt.plot(0, 1.5, 'ko', label='f(0) = 1.5')

plt.legend()

plt.show()
