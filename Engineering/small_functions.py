# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 9.16 LAB: Small Functions
# Date:  10/25/22

from math import pi, ceil

# Part A
def parta(radius_sphere, radius_hole):
    total_volume = (4 / 3) * pi * (radius_sphere**3)
    cylinder_height = radius_sphere * 2
    print(total_volume)
    print(radius_hole**2)
    print(pi*cylinder_height)
    cylinder_volume = (pi * cylinder_height) * (radius_hole**2)
    print(total_volume)
    print(cylinder_volume)
    # subtracts hole from total
    total_volume=abs(total_volume)
    cylinder_volume=abs(cylinder_volume)
    total_volume-= cylinder_volume
    return total_volume


print(parta(1,0.95))


# Part B
def partb(number):
    # Variables
    total = 0
    output_list = []
    starting_number = 1
    current_number = 1

    # Loop
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


# Part C
def partc(char, name, company, email):
    all_list = [name, company, email]

    print(max(all_list, key=len))
    length = len(max(all_list, key=len))

    # finds spaces
    line1_space = int(((length - (len(name))) / 2) + 2)
    line2_space = int(((length - (len(company))) / 2) + 2)
    line3_space = int(((length - (len(email))) / 2) + 2)

    # checks if odd
    if length % 2 == 0 and len(name) % 2 != 0:
        name = name + " "
    if length % 2 == 0 and len(company) % 2 != 0:
        company = company + " "
    if length % 2 == 0 and len(email) % 2 != 0:
        email = email + " "

    card = f"{char*(length+6)}\n{char}{' '*line1_space}{name}{' '*(line1_space)}{char}\n{char}{' '*(line2_space)}{company}{' '*(line2_space)}{char}\n{char}{' '*line3_space}{email}{' '*(line3_space)}{char}\n{char*(length+6)}"
    return card


# Part D
def partd(numbers):
    numbers.sort()
    # checks if odd
    if len(numbers) % 2 != 0:
        median = numbers[ceil(len(numbers) / 2) - 1]
    else:
        median = numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2) - 1]
        if median == 0:
            median = int(median)

    minimum = numbers[0]
    maximum = numbers[-1]
    return minimum, median, maximum


# Part E
def parte(times, distances):
    # variables
    velocity_list = []
    for x in range(len(times) - 1):
        velocity_list.append((distances[x + 1] - distances[x]) / (times[x + 1] - times[x]))
    return velocity_list


# Part F
def partf(numbers):
    target = 2026
    i = 0
    # loop
    while i < len(numbers):
        for x in range(len(numbers)):
            if numbers[i] + numbers[x] == 2026:
                return numbers[i] * numbers[x]
        i += 1
    else:
        return False
