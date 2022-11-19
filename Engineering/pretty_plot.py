# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Evan Slyter
# Section:      565
# Assignment:   12.16 LAB: Pretty Plot
# Date:         11/18/22

# importing modules
import numpy as np
import matplotlib.pyplot as plt

# making the point and initial array
point_v = np.array([(0), (1)])
x = np.array([0])
y = np.array([1])
matrix = np.array([(1.01, 0.09), (-0.09, 1.01)])


# multiplies everything
for i in range(200):
    prod = point_v @ matrix
    point_v = prod
    x = np.append(x, point_v[0])
    y = np.append(y, point_v[1])

# makes the plit
plt.plot(x, y, "b--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Super cool spiral")
plt.show()
