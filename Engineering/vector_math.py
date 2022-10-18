# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 7.27 LAB: Vector Math
# Date: 10/17/22

# imports square root from math
from math import sqrt

#
vector_A = input("Enter the elements for vector A: ")
vector_A = vector_A.split()
vector_B = input("Enter the elements for vector B: ")
vector_B = vector_B.split()

# turns all elements in a list to floats
def turn_float(list):
    for x in range(len(list)):
        list[x] = float(list[x])


# gets magnitude of a single vector
def magnitude(list):
    square_total = 0
    for x in range(len(list)):
        square_total += list[x] ** 2
    return sqrt(square_total)


# gets sum of two vectors
def sum(list1, list2):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] + list2[x])
    return list3


# gets difference between two vectors
def difference(list1, list2):
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] - list2[x])
    return list3


# gets dot product of two vectors
def dot_product(list1, list2):
    total = 0
    list3 = []
    for x in range(len(list1)):
        list3.append(list1[x] * list2[x])

    for x in range(len(list3)):
        total += list3[x]
    return total


turn_float(vector_A)
turn_float(vector_B)

print(f"The magnitude of vector A is {magnitude(vector_A):.5f}")
print(f"The magnitude of vector B is {magnitude(vector_B):.5f}")

print(f"A + B is {sum(vector_A,vector_B)}")
print(f"A - B is {difference(vector_A,vector_B)}")

print(f"The dot product is {dot_product(vector_A,vector_B):.2f}")
