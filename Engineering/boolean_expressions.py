# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: Evan Slyter
#        Sam Kinnard
#        Caleb Lorimor
#        Ryan Kethley
# Section:   565
# Assignment: 4.15 LAB: Boolean expressions
# Date: 9/20/22

############ Part A ############
# inputs
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

# sets variables true or false
a = "t" in a or "T" in a or "True" in a or "true" in a
b = "t" in b or "T" in b or "True" in b or "true" in b
c = "t" in c or "T" in c or "True" in c or "true" in c

############ Part B ############
f1 = a and b and c

f2 = a or b or c

print(f"a and b and c: {f1}")

print(f"a or b or c: {f2}")

############ Part C ############
f3 = a and not b or not a and b

f4 = a and (not b and not c) or b and (not a and not c) or c and (not a and not b) or (a and b and c)

print(f"XOR: {f3}")

print(f"Odd number: {f4}")
