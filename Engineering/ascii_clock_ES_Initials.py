# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 8.10 LAB: ASCII Clock
# Date: 10/23/22

e = [
    ["E", "E", "E"],
    ["E", " ", " "],
    ["E", "E", "E"],
    ["E", " ", " "],
    ["E", "E", "E"],
]

s = [
    ["S", "S", "S"],
    ["S", " ", " "],
    ["S", "S", "S"],
    [" ", " ", "S"],
    ["S", "S", "S"],
]

initials = [e, s]

# all the printing
print("\n", end="")
for row in range(5):
    for letter in range(2):
        for digit in range(3):
            if digit == (2) and letter == (1):
                print(f"{(initials[letter])[row][digit]}", end="\n")
            else:
                print(f"{(initials[letter])[row][digit]}", end="")
            if digit == (2) and letter == (0):
                print(" ", end="")
