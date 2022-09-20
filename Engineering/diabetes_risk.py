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

sex = input("Enter your sex (M/F): ") 
age = float(input("Enter your age (years): "))
BMI = float(input("Enter your BMI: "))
meds = input("Are you on medication for hypertension (Y/N)? ")
roids = input("Are you on steroids (Y/N)? ") 
cig = input("Do you smoke cigarettes (Y/N)? ")
smoke = input("Did you used to smoke (Y/N)? ")
history = input("Do you have a family history of diabetes (Y/N)? ")


if sex == 'M':
  sex = 0
elif sex == 'F':
  sex = 0.879


if BMI<25:
  BMI=0
elif BMI <=27.49:
  BMI=0.699
elif BMI<= 29.99:
  BMI=1.97
elif BMI >= 30:
  BMI = 2.518


if meds == 'Y' or meds == 'y':
  meds = 1.222
else:
  meds = 0


if roids == 'Y' or roids == 'y':
  roids = 2.191 
else:
  roids = 0

if cig=='Y' or cig == 'y':
  cig=0.855
elif smoke=='Y' or smoke=='y':
  cig= -0.218
else:
  cig=0

if history=='Y' or history=='y':
  familyor = input("Was it from a parent or sibling (Y/N)? ");
  if familyor=='Y' or familyor=='y':
      history=0.728
      familyand = input('Was it both a parent and a sibling (Y/N)? ')
      if familyand == 'Y' or familyand == 'y':
        history = 0.753
      else:
        history = 0.728
else:
  history = 0
      

risk=100/(1+e**(6.322+sex-(0.063*age)-BMI-meds-roids-cig-history))

print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')

