# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment:
# Date:
from math import sqrt

sl = float(input("Enter the side length in meters: "))
layer = int(input("Enter the number of layers: "))


howmany = 0
totalsa = 0

for x in range(1, layer + 1):
    howmany = howmany + ((1 * x - 1) + x)
    # sa of outside band
    s = ((sl * x) * 3) * sl
    # sa of outside band + top
    sa = s + (((sqrt(3) / 4) * ((sl * x) ** 2)))

    totalsa = totalsa + sa
    totalsa = totalsa - ((sqrt(3) / 4) * ((sl * (x - 1)) ** 2))

print(f"You need {totalsa:.2f} m^2 of gold foil to cover the pyramid")
