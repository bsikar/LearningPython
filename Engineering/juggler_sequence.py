# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 6.13 LAB: Howdy Whoop
# Date:  10/6/22

# imports math for sqaure root
import math

# defining variables
input = int(input("Enter a positive integer: "))
num = input
count = 0

# prints the beginning part
print(f"The Juggler sequence starting at {input} is: ")
if input == 1:
    print(input)
else:
    print(input, end=", ")
# prints the middle part
while num != 1:
    count += 1

    if num % 2 == 0:
        num = int(math.sqrt(num))

    else:
        num = num**3
        num = int(math.sqrt(num))

    if num == 1:
        print(num)
    else:
        print(num, end=", ")
# prints the end part
print(f"It took {count} iterations to reach 1")
