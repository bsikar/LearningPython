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

A = np.arange(12).reshape(3, 4)
print("A =", A, "\n")

B = np.arange(8).reshape(4, 2)
print("B =", B, "\n")

C = np.arange(6).reshape(2, 3)
print("C =", C, "\n")

D = A @ B @ C
print("D =", D, "\n")

DT = np.transpose(D)
print("D^T =", DT, "\n")

E = np.sqrt(D) / 2
print("E =", E)
