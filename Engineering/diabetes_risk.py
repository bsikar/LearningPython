# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Names: Evan Slyter
#        Sam Kinnard
#        Caleb Lorimor
#        Ryan Kethley
# Section:   565
# Assignment: 5.3: Diabetes Risk
# Date: 9/20/22

from math import *

# entering values for every single possible factor in diabetes likelihood
sex = input("Enter your sex (M/F): ") 
age = float(input("Enter your age (years): "))
BMI = float(input("Enter your BMI: "))
meds = input("Are you on medication for hypertension (Y/N)? ")
roids = input("Are you on steroids (Y/N)? ") 
cig = input("Do you smoke cigarettes (Y/N)? ")
smoke = 0

# determining the parameter based on sex
if sex == 'M' or sex=="m":
  sex = 0
elif sex == 'F' or sex=="f":
  sex = 0.879

# determining parameter based on body mass index
if BMI < 25:
  BMI = 0
elif BMI <= 27.49:
  BMI = 0.699
elif BMI <= 29.99:
  BMI = 1.97
elif BMI >= 30:
  BMI = 2.518

# determining parameter based on hypertension medication
if meds == 'Y' or meds == 'y':
  meds = 1.222
elif meds == 'N' or meds == 'n':
  meds = 0

# determining parameter based on steroid use
if roids == 'Y' or roids == 'y':
  roids = 2.191 
elif roids == 'N' or roids == 'n':
  roids = 0

# determining parameter based on cigarette use
if cig == 'Y' or cig == 'y':
  cig = 0.855
elif cig == 'N' or cig == 'n':
    smoke = input("Did you used to smoke (Y/N)? ")
    if smoke == 'Y' or smoke == 'y':
        cig = -0.218
    elif smoke == 'N' or smoke == 'n':
        cig = 0

# establishing history variable after the smoking if block
# so that the program will ask questions in the right order
history = input("Do you have a family history of diabetes (Y/N)? ")

# determining the parameter for family diabetes history
if history == 'Y' or history == 'y':
  family_and = input("Both parent and sibling (Y/N)? ")
  if family_and == 'Y' or family_and == 'y':
      history = 0.753
  elif family_and == 'N' or family_and == 'n':
        history = 0.728
elif history == 'N' or history =='n':
  history = 0

# risk equation using values determined by conditional blocks above

risk=100/(1+e**(6.322+sex-(0.063*age)-BMI-meds-roids-cig-history))

print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')

