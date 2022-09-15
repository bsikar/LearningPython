# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: 3.18 LAB: Calling Functions
# Date: 9/15/22 

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

side=float(input("Please enter the side length: "))

triangleArea=((sqrt(3))/(4))*(side**2)

squareArea=side**2

pentagonArea=(0.25)*sqrt((5)*(5+(2*sqrt(5))))*(side**2)

dodecagonArea=(3)*(2+sqrt(3))*(side**2)

printresult("triangle",side,triangleArea)

printresult("square",side,squareArea)

printresult("pentagon",side,pentagonArea)

printresult("dodecagon",side,dodecagonArea)

# example function call:
# printresult(<string of shape name>, <float of area>, <float of side>)
# printresult('square', 5, 2.236)
# Your code goes here