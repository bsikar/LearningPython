# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: 4.19 LAB: Calculate Roots
# Date:  9/23/22

#inputs
a=float(input("Please enter the coefficient A: "))
b=float(input("Please enter the coefficient B: "))
c=float(input("Please enter the coefficient C: "))


if a==0 and b!=0:
    f1=float((-1*c)/b)
    f2=((-1*c)/b)

elif a==0 and b==0:
    print("You entered an invalid combination of coefficients!")
    quit()
    
else:
    f1=(-1*b+((b**2)-((4*a)*c))**0.5)/(2*a)

    f2=(-1*b-((b**2)-((4*a)*c))**(0.5))/(2*a)


#checks for multiple roots
if (f1) == (f2):

    #checks for imaginary numbers
    if "j" in str(f1):
        if f1.imag < 0:
            sign="-"
        else:
            sign="+"
        print(f"The root is x = {f1.real} {sign} {abs(f1.imag)}i")
            
    else:
        print(f"The root is x = {float(f1):.1f}")

else:
    
    #checks for imaginary numbers
    if "j" in str(f1):
        if f1.imag < 0:
            sign1="-"
        else:
            sign1="+"
        
        if f2.imag < 0:
            sign2="-"
        else:
            sign2="+"

        print(f"The roots are x = {f1.real} {sign1} {abs(f1.imag)}i and x = {f2.real} {sign2} {abs(f2.imag)}i")
        
    else:
        print(f"The roots are x = {float(f1):.1f} and x = {float(f2):.1f}")








    
