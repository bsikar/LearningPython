# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
#         Ryan Kethley
#         Caleb Lorimor
#         Sam Kinnard
# Section:   565
# Assignment: 12.14 LAB: Numpy Example
# Date: 11/15/22

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import numpy as np
from numpy import linspace, pi
import matplotlib.pyplot as plt

# 1st plot
x = np.arange(-2.0, 2.0, 0.01)
y = 1 / (4 * 6) * x**2
y1 = 1 / (4 * 2) * x**2

plt.title("Parabola plots with varying focal length")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1, color="red", linewidth=1, label="f = 2")
plt.plot(x, y, color="blue", linewidth=5, label="f = 6")
plt.legend(loc="lower left")
plt.show()

# 2nd plot

x = np.arange(-4, 4, 0.33)
y = 2 * x**3 + (3 * x**2) - (11 * x) + 6
plt.title("Plot of cubic polynomial")
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.scatter(x, y, color="yellow", marker="*", edgecolors="black", s=100)
plt.show()

# 3rd plot

x = np.arange(-2 * pi, 2 * pi, 0.1)
y = np.sin(x)
y1 = np.cos(x)

fig, axes = plt.subplots(2, figsize=(16, 5))
axes[0].plot(x, y1, label="cos(x)", color="maroon")
axes[0].set(ylabel="y=cos(x)")
axes[0].legend(loc="lower right")
axes[1].plot(x, y, label="sin(x)", color="gray")
axes[1].set(ylabel="y=sin(x)")
axes[1].legend(loc="upper right")
plt.xlabel("x")

plt.suptitle("Plot of cos(x) and sin(x)")
plt.show()
