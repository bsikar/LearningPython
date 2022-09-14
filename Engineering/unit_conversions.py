# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Names: Evan Slyter
#        Sam Kinnard
#        Caleb Lorimor
#        Ryan Kethley

# Section:   565
# Assignment: 3.15 LAB: Unit Conversions
# Date:  9/8/22

input=input("Please enter the quantity to be converted:\n")
input=float(input)

#converts pounds to newtons
def pounds_Newtons(input):
    print(f"{float(input):.2f} pounds force is equivalent to {float(input)*4.44822:.2f} Newtons")

#converts meters to feet
def meters_Feet(input):
    print(f"{float(input):.2f} meters is equivalent to {float(input)*3.28084:.2f} feet")
    
#converts atmosphere to kilopascal
def atmosphere_Kilopascal(input):
    print(f"{float(input):.2f} atmospheres is equivalent to {float(input)*101.325:.2f} kilopascals")
    
#converts watts to kilopascal
def watts_BTU(input):
    print(f"{float(input):.2f} watts is equivalent to {float(input)*3.41214:.2f} BTU per hour")
    
#converts liters to gallons
def liters_Gallons(input):
    print(f"{float(input):.2f} liters per second is equivalent to {float(input)*15.850323141489:.2f} US gallons per minute")
    
#converts celsius to fahrenheit
def celsius_Fahrenheit(input):
    print(f"{float(input):.2f} degrees Celsius is equivalent to {(float(input)*1.8)+32:.2f} degrees Fahrenheit")
    
pounds_Newtons(input)

meters_Feet(input)

atmosphere_Kilopascal(input)

watts_BTU(input)

liters_Gallons(input)

celsius_Fahrenheit(input)
    
