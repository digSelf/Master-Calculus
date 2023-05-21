import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
fx = lambda x : 3 * x**2 - 3 * x + 4
dfx = lambda x : 6 * x - 3 

x = np.arange(-2, 2, step=dx)

def gradient_descent(dfx, l, r):
    start = np.random.randint(l, r)
    x = start
    epochs = 100
    m = .01

    result = [x]
    for i in range(epochs):
        x = x - m * dfx(x)
        result.append(x)
    
    return np.array(result)

xs = gradient_descent(dfx, -2, 2)

plt.plot(x, fx(x), label='f(x)')
plt.plot(x, dfx(x), label='df(x)')

plt.scatter(xs, fx(xs))
plt.scatter(xs, dfx(xs))

plt.grid()
plt.show()
