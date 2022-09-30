# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 5.4 LAB: Boiling Curve
# Date:  9/30/22

from math import log

# input for excess temperature
excessTemp = float(input("Enter the excess temperature: "))

# assigning the variables some numbers
if 1.3 <= excessTemp < 5:
    x0 = 1.3
    x1 = 5
    y0 = 1000
    y1 = 7000
elif 5 <= excessTemp < 30:
    x0 = 5
    x1 = 30
    y0 = 7000
    y1 = 1.5e6
elif 30 <= excessTemp < 120:
    x0 = 30
    x1 = 120
    y0 = 1.5e6
    y1 = 2.5e4
elif 120 <= excessTemp <= 1200:
    x0 = 120
    x1 = 1200
    y0 = 2.5e4
    y1 = 1.5e6
# if the user puts an unexpected excessTemp
else:
    print("Surface heat flux is not available")
    exit()

# calculates m for the next equation
m = (log(y1 / y0)) / (log(x1 / x0))
# calculates surface heat flux
y = y0 * (excessTemp / x0) ** m
print(f"The surface heat flux is approximately {round(y)} W/m^2")
