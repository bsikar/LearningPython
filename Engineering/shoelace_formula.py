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


vertices = input("Please enter the vertices: ")
cross_list=[]


def getpoints(string):
  string=string.split()
  for x in range(len(string)):
      string[x]=string[x].split(',')
      for y in range(len(string[x])):
        string[x][y]=int(string[x][y])
  return string
  

def cross(p1,p2):
  product=(p1[0]*p2[1])-(p2[0]*p1[1])
  return product

for x in range(len(getpoints(vertices))-1):
    cross_list.append(cross(getpoints(vertices)[x],getpoints(vertices)[x+1]))
cross_list.append(cross(getpoints(vertices)[-1],getpoints(vertices)[0]))

area=(0.5)*sum(cross_list)
print(area)

def shoelace():
  area 
  print()


def main():
  print()

