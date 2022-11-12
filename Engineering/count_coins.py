# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 11.12 LAB: Counting Coins
# Date: 11/11/22

# opems files and creates variables
game_file = open("game.txt", "r")
coins_file = open("coins.txt", "w")
game = game_file.read()
game = game.split("\n")
position = 0
coins = 0

# does what the game says
while position < len(game):
    if "coin" in game[position]:
        number = game[position][5:]
        if "+" in number:
            number = int(number[1:])
        elif "-" in number:
            number = (int(number[1:])) * -1
        coins_file.write(str(number))
        coins_file.write("\n")
        coins += number
        position += 1
    elif "jump" in game[position]:
        number = game[position][5:]
        if "+" in number:
            number = int(number[1:])
        elif "-" in number:
            number = (int(number[1:])) * -1
        position += number
    elif "none" in game[position]:
        position += 1

# prints final coin count
print(f"Total coins collected: {coins}")

# closes files
coins_file.close()
game_file.close()
