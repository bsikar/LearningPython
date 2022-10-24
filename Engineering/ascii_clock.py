# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 8.10 LAB: ASCII Clock
# Date: 10/23/22

# inputs
user_input = input("Enter the time: ")
user_list = []

# breaks input into list
for x in range(len(user_input)):
    user_list.append(user_input[x])
if len(user_list) == 4:
    user_list = ["0"] + user_list
user_list.pop(2)


# numbers
one = [
    [" ", "1", " "],
    ["1", "1", " "],
    [" ", "1", " "],
    [" ", "1", " "],
    ["1", "1", "1"],
]

two = [
    ["2", "2", "2"],
    [" ", " ", "2"],
    ["2", "2", "2"],
    ["2", " ", " "],
    ["2", "2", "2"],
]

three = [
    ["3", "3", "3"],
    [" ", " ", "3"],
    ["3", "3", "3"],
    [" ", " ", "3"],
    ["3", "3", "3"],
]

four = [
    ["4", " ", "4"],
    ["4", " ", "4"],
    ["4", "4", "4"],
    [" ", " ", "4"],
    [" ", " ", "4"],
]

five = [
    ["5", "5", "5"],
    ["5", " ", " "],
    ["5", "5", "5"],
    [" ", " ", "5"],
    ["5", "5", "5"],
]

six = [
    ["6", "6", "6"],
    ["6", " ", " "],
    ["6", "6", "6"],
    ["6", " ", "6"],
    ["6", "6", "6"],
]

seven = [
    ["7", "7", "7"],
    [" ", " ", "7"],
    [" ", " ", "7"],
    [" ", " ", "7"],
    [" ", " ", "7"],
]

eight = [
    ["8", "8", "8"],
    ["8", " ", "8"],
    ["8", "8", "8"],
    ["8", " ", "8"],
    ["8", "8", "8"],
]

nine = [
    ["9", "9", "9"],
    ["9", " ", "9"],
    ["9", "9", "9"],
    [" ", " ", "9"],
    ["9", "9", "9"],
]

zero = [
    ["0", "0", "0"],
    ["0", " ", "0"],
    ["0", " ", "0"],
    ["0", " ", "0"],
    ["0", "0", "0"],
]

riley = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

# riley
if user_list[0] == "0":
    user_list[0] = "riley"

# dictionary for numbers
numbers = {
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
    "0": zero,
    "riley": riley,
}

# all the printing
print("\n", end="")
for row in range(5):
    for number in range(4):
        if user_list[number] == "riley":
            number += 1
            continue
        for digit in range(3):
            if number == (3) and digit == (2):
                print(f"{(numbers[user_list[number]])[row][digit]}", end=" \n")
            else:
                print(f"{(numbers[user_list[number]])[row][digit]}", end="")
            if digit == (2) and number != (3):
                print(" ", end="")
            if row != (1) and row != (3) and number == (1) and digit == (2):
                print("  ", end="")
            if row == (1) and number == (1) and digit == (2):
                print(": ", end="")
            if row == (3) and number == (1) and digit == (2):
                print(": ", end="")
