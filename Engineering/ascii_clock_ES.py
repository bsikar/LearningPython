# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
#         Ryan Kethley
#         Caleb Lorimor
#         Sam Kinnard
# Section:   565
# Assignment: 8.10 LAB: ASCII Clock
# Date: 10/24/22

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

# replaces 0 with an empty list named riley
# if user_list[0] == "0":
#    user_list[0] = "riley"

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
