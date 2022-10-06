# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: 4.16 LAB: Largest Number
# Date: 9/20/22 

#numbers to be tested
num1=float(input("Enter number 1: "))
num2=float(input("Enter number 2: "))
num3=float(input("Enter number 3: "))


biggest=0

#checks which number is biggest
if num1 >= num2 and num1>=num3:
    biggest=num1

if num2>= num1 and num2>= num3:
    biggest=num2

if num3>= num2 and num3>= num1:
    biggest=num3

print(f"The largest number is {biggest}")