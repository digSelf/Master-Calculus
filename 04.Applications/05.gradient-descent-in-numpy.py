import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
fx = lambda x : 3 * x**2 - 3 * x + 4
dfx = lambda x : 6 * x - 3 

x = np.arange(-2, 2, step=dx)

def gradient_descent(fx, dfx, l, r):
    start = np.random.randint(l, r)
    x = start
    epochs = 100
    m = .01

    for i in range(epochs):
        x = x - m * dfx(x)
    
    return x, fx(x) 

xn, val = gradient_descent(fx, dfx, -2, 2)
print("the f(x) gets the minimum {} at x = {}".format(val, xn))