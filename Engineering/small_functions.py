# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 9.16 LAB: Small Functions
# Date:  10/25/22

from math import pi, ceil


def parta(radius_sphere, radius_hole):
    total_volume = (4 / 3) * pi * (radius_sphere**3)
    cylinder_height = radius_sphere * 2
    cylinder_volume = pi * cylinder_height * (radius_hole**2)
    total_volume -= cylinder_volume
    return total_volume


def partb(number):
    # total = 0
    # beginning = 1
    # output_list = []
    # while total != number:
    #    for x in range(beginning, number, 2):
    #       total += x
    #      output_list.append(x)
    #     print(output_list)
    #    if total > number:
    #       total = 0
    #      output_list = []
    #     beginning += 2
    #    x=beginning
    # if total == number:
    #   return output_list
    # else:
    # return False
    total = 0
    output_list = []
    starting_number = 1
    current_number = 1

    while starting_number < number:
        total += current_number
        output_list.append(current_number)
        if total > number:
            total = 0
            output_list = []
            starting_number += 2
            current_number = starting_number
            current_number -= 2
        if total == number:
            return output_list
        current_number += 2
    else:
        return False


def partc(char, name, company, email):
    all_list = [name, company, email]
    length = len(max(all_list, key=len))
    if len(name) % 2 != 0:
        name += " "
    if len(company) % 2 != 0:
        company += " "
    if len(email) % 2 != 0:
        email += " "
    line1_space = int(((length - (len(name))) / 2) + 2)
    line2_space = int(((length - (len(company))) / 2) + 2)
    line3_space = int(((length - (len(email))) / 2) + 2)
    card = f"{char*(length+6)}\n{char}{' '*line1_space}{name}{' '*line1_space}{char}\n{char}{' '*line2_space}{company}{' '*line2_space}{char}\n{char}{' '*line3_space}{email}{' '*line3_space}{char}\n{char*(length+6)}"
    return card


def partd(numbers):
    numbers.sort()
    minimum = numbers[0]
    median = numbers[ceil(len(numbers) / 2)]
    maximum = numbers[-1]
    return minimum, median, maximum
