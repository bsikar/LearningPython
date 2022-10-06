# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 6.13 LAB: Howdy Whoop
# Date:  10/6/22

# variables
leftSum = 0
right_sum = 0
r = 1
n = int(input("Enter a value for n: "))
n1 = n

# loop to find sum of all numbers before n
for x in range(n):
    leftSum = leftSum + x

# loop to find if n is a balancing number
while right_sum <= leftSum:
    n1 += 1
    right_sum += n1

    if right_sum == leftSum:
        print(f"{n} is a balancing number with r={r}")
        exit()
    r += 1

# prints if the loop ends
else:
    print(f"{n} is not a balancing number")
