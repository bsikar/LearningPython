# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Names: Evan Slyter
#        Sam Kinnard
#        Caleb Lorimor
#        Ryan Kethley
# Section:   565
# Assignment: 4.13 LAB: Make Change
# Date:  9/13/22

payment=float(input("How much did you pay? "))
cost=float(input("How much did it cost? "))
change=round((payment-cost),2)
quarters=0
dimes=0
nickels=0
pennies=0
print(f"You received ${change:.2f} in change. That is... ")

while (change>0):
    if change>=0.25:
        quarters+=1
        change-=0.25
        change=round(change,2)
        #print(change)
        
    elif change>=0.10:
        dimes+=1
        change-=0.10
        change=round(change,2)
        #print(change)

    elif change>=0.05:
        nickels+=1
        change-=0.05
        change=round(change,2)
        #print(change)
    else:
        pennies+=1
        change-=0.01
        change=round(change,2)
        #print(change)


if quarters>0:
    if quarters==1:
        print(f"{quarters} quarter")
    else:
        print(f"{quarters} quarters")


if dimes>0:
    if dimes==1:
        print(f"{dimes} dime")
    else:
        print(f"{dimes} dimes")
 


if nickels>0:
    if nickels==1:
        print(f"{nickels} nickel") 
    else:
        print(f"{nickels} nickels")

     
   
if pennies>0.1:
    if pennies==1:
        print(f"{pennies} penny")
    else:
        print(f"{pennies} pennies")



    
