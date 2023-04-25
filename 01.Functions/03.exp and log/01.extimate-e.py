import numpy as np

# domain n: [1, +infty]
f = lambda n : (1 + 1/n)**n

n = np.linspace(1, 50)
for i in n:
    y = f(i)
    print(f"n: {int(i)},\test.e: {y: .5f},\tdiff to e: {np.e - y: .5f}")

