# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 7.25 LAB: Pig latin
# Date: 10/14/22

# getting original input and putting each word into a list
user_input = input("Enter word(s) to convert to Pig Latin: ")
user_list = user_input.split()

# function to turn any word into the pig latin version of the word
def pigify(word):

    vowels = ["a", "e", "i", "o", "u", "y"]

    if word[0] in vowels:
        return word + "yay"
    elif word[0] not in vowels and word[1] in vowels:
        return word[1:] + word[0] + "ay"
    else:
        return word[2:] + word[0:2] + "ay"


# prints the beginning of the sentence
print(f'In Pig Latin, "{user_input}" is: ', end="")


for x in range(len(user_list)):
    user_list[x] = pigify(user_list[x])
    print(user_list[x], end=" ")
