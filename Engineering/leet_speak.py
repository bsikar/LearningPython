# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 7.26 LAB: Leet Speak
# Date: 10/17/22

# inputs
user_words = input("Enter some text: ")
user_list = user_words.split()

# function to leetify
def leetify(list):
    leetletters = {"a": "4", "e": "3", "o": "0", "s": "5", "t": "7"}

    for x in range(len(list)):
        for y in range(len(list[x])):
            if user_list[x][y] in leetletters:
                user_list[x] = user_list[x].replace(user_list[x][y], leetletters[user_list[x][y]])


# first part of print
print(f'In leet speak, "{user_words}" is:', end=" ")
# map(SOME_FUNCTION, SOMETHING_THAT_RETURNS_SOMETHING_THAT_CAN_BE_ITERATED)
# map(function, iterator)
# second part of print
for x in range(len(user_list)):
    leetify(user_list)
    print(user_list[x], end=" ")
