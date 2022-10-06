# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 6.13 LAB: Howdy Whoop
# Date:  10/6/22

# inputs for numbers
num1 = float(input("Enter an integer: "))
num2 = float(input("Enter another integer: "))

# loop to print everything
for x in range(1, 101):
    if x % num1 == 0 and x % num2 == 0:
        print("Howdy Whoop")
    elif x % num1 == 0:
        print("Howdy")
    elif x % num2 == 0:
        print("Whoop")
    else:
        print(x)
