from pprint import pprint
import numpy as np

fx = lambda x : (np.cos(x ** 2) ** 2) + np.pi

# from the left side of the point x = 1
iter_bound = 20
x = 0  # a - 1

left_side_values = []
for i in range(iter_bound):
    left_side_values.append([x, fx(x)])
    x = (x + 1) / 2

print("Limit from the left: ")
pprint(left_side_values)

# from the right side of the point x = 1
x = 2
right_side_values = []
for i in range(iter_bound):
    right_side_values.append([x, fx(x)])
    # x = x - (x -  1) / 2 -> x = (x + 1) / 2
    x = (x + 1) / 2

print("Limit from the right:")
pprint(right_side_values)

print(f"\nFunction value at x = 1: {fx(1)}")