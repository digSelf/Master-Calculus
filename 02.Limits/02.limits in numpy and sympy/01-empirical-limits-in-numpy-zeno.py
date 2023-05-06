import numpy as np
import matplotlib.pyplot as plt

fx = lambda x : np.cos(x * np.pi) + np.log(x) ** 2

x = np.linspace(1e-5, 2 * np.pi, 1000)

# plot the function
plt.plot(x, fx(x))
plt.grid()

plt.xlim((0, 2 * np.pi))
plt.ylim((-1.5, 2 * np.pi))

plt.show()
plt.close()

# estimate the limit of the function as x approaces 3
# 1) zoom in 
plt.plot(x, fx(x), 'k-', label='y = f(x)')
plt.grid()
plt.xlim((1, 5))
plt.ylim((-1.5, 2 * np.pi))

# 2) define a function of approaching
def approaching(start, target, f):
    iter_bound = 20
    x0 = start
    
    xs = []
    ys = []
    for i in range(iter_bound):
        y = f(x0)
        xs.append(x0)
        ys.append(y)
        x0 = x0 + (target - x0) / 2

    return np.array(xs), np.array(ys)

# 2.1) log the pair of (x, f(x)) from the left of x-axis approaching 3 
target = 3
start = target - 1  # [2, 3)
left_xs, left_side_values = approaching(start, target, fx)

# 2.2) from the right side
start = target + 1  # (3, 4]
right_xs, right_side_values = approaching(start, target, fx)

# 3) output the estimate values
print(f"limit approaches {left_side_values[-1]} from the left.")
print(f"limit approaches {right_side_values[-1]} from the right.")

# 4) plot the trace
plt.plot(left_xs, left_side_values, 'o', markerfacecolor='w', label='from the left')
plt.plot(right_xs, right_side_values, 'o', markerfacecolor='w', label='from right')

plt.title(f'function value at x = 3 is {fx(3)}')

plt.legend()
plt.show()

