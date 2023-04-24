import numpy as np
import matplotlib.pyplot as plt

domain = [-50, 50]

# generate random coefficients from the standard normal distribution
coefficients = np.random.randn(4)

# The numpy.linspace function returns evenly spaced numbers over a specified interval. 
# It returns num evenly spaced samples, calculated over the interval [start, stop]. 
# The endpoint of the interval can optionally be excluded 1. 
# For example, numpy.linspace(2.0, 3.0, num=5) would return an array of 5 evenly spaced numbers 
# between 2.0 and 3.0: [2. , 2.25, 2.5 , 2.75, 3.] <- step = (3.0 - 2.0) / (5 - 1) = 0.25
# sampling to get the input values.
x = np.linspace(start=domain[0], stop=domain[-1])  # sampling

# define the polynomial and generate the output values.
label = "$y ="
y = .0 
for i, c in enumerate(coefficients):
    y += c * x ** i
    label += '+ '[int(c < 0)] + f'{c: .2f}x^{i} ' 

label += "$"
plt.plot(x, y, label=label)

plt.grid()
plt.legend()
plt.xlim((domain[0], domain[-1]))
plt.xlabel('x')
plt.ylabel('y = f(x)')

plt.show()







