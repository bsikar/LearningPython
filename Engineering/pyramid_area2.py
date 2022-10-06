# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment:
# Date:
from math import sqrt

sl = float(input("Input side length"))
layer = int(input("Input number of layers"))

# howmany=howmany + ((1*layer-1)+layer)


totalsa = 0

for x in range(1, layer):
    # sa of outside band
    s = ((sl * layer) * 3) * sl

    # sa of outside band + top
    sa = s + ((sqrt(3) / 4) * (sl**2)) * (sl * layer)

    totalsa = totalsa + sa
    totalsa = totalsa - (sqrt(3) / 4) * (sl**2)
print(totalsa)
