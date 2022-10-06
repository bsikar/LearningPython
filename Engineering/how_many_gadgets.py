# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: 4.18 LAB: How many gadgets
# Date: 9/20/22 
day=int(input("Please enter a positive value for day: "))

#function for finding the gadgets

def gadgets(day):
    #first 10 days
    if day<=10:
        return day * 5
    #11-60
    if day<=60:
        return 50 + gadgets(day - 1)
    #61-100
    if day<=100:
        return 110 - day + gadgets(day -1)
    
    return gadgets(day-1)

#checks for valid day
if day<=0:
    print("You entered an invalid number!")    
else:
    print(f"The total number of gadgets produced on day {day} is {gadgets(day)}")    