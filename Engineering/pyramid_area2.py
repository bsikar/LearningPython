# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
#         Ryan Kethley
#         Caleb Lorimor
#         Sam Kinnard
# Section:   565
# Assignment: Pyramid Area 2
# Date: 10/7/22

# imports
from math import *

# variables
side = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))

layers = (n * ((n + 1) / 2)) * 3 * (side**2)

top = (n**2) * (sqrt(3) / 4) * (side**2)

total_area = layers + top

print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")
