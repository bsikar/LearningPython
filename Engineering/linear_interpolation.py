# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Names:  Evan Slyter
#         Jeevan Arianayagam
#         Chris Avila
#         Darian Kanu
# Section:   565
# Assignment: LAB 2.8: Linear Interpolation
# Date:  9/8/7

import math

#part1
Time_Passed=25
ISS_Position=((21000/45)*(Time_Passed-10)+2026)

print("Part 1: \nFor t = 25 minutes, the position p =", ISS_Position, "kilometers")

#part 2

Earth_Circ=2*math.pi*6745
Time_Passed=300
ISS_Poswithreset = (((21000/45)*(Time_Passed-10)+2026)%(Earth_Circ))

print("Part 2: \nFor t = 300 minutes, the position p =", ISS_Poswithreset," kilometers")