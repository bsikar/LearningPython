# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
#         Ryan Kethley
#         Caleb Lorimor
#         Sam Kinnard
# Section:   565
# Assignment: 9.15 LAB: Shoelace formula
# Date: 10/25/22

# getpoints function
def getpoints(string):
    string = string.split()
    for i in range(len(string)):
        a = string[i].split(",")
        for k in range(len(a)):
            a[k] = float(a[k])
        string[i] = a
    return string


def cross(p1, p2):
    p1X = p1[0]
    p1Y = p1[1]
    p2X = p2[0]
    p2Y = p2[1]
    product = (p1X * p2Y) - (p1Y * p2X)
    return product


def shoelace(vertices):
    vertices.append(vertices[0])
    total = 0
    for i in range(len(vertices) - 1):
        total += (cross(vertices[i], vertices[i + 1])) / 2
    return total


def main():
    vertices = input("Please enter the vertices: ")
    vertices = getpoints(vertices)
    area = shoelace(vertices)
    print("The area of the polygon is ", area)


if __name__ == "__main__":
    main()
