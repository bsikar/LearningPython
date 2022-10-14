# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
#         Ryan Kethley
#         Caleb Lorimor
#         Sam Kinnard
# Section:   565
# Assignment: Go_Moves
# Date: 10/13/22
board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
row = 0
column = 0


def print_array(array):
    x = 0
    y = 0
    while x <= 8:
        while y <= 8:
            print(array[x][y], end=" ")
            y += 1
        print("\n")
        y = 0
        x += 1


def black():
    print("Black's turn")
    row = int(input("Input row number: "))
    column = int(input("Input column number: "))
    if board[row - 1][column - 1] == ".":
        board[row - 1][column - 1] = chr(9675)
        print_array(board)
    else:
        print("Spot occupied, please choose a differnt spot.")
        black()


def white():
    print("White's turn")
    row = int(input("Input row number: "))
    column = int(input("Input column number: "))
    if board[row - 1][column - 1] == ".":
        board[row - 1][column - 1] = chr(9679)
        print_array(board)
    else:
        print("Spot occupied, please choose a different spot.")
        white()


print_array(board)

while row != "stop" and column != "stop":
    black()
    white()
