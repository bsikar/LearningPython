# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Names: Evan Slyter
#        Sam Kinnard
#        Caleb Lorimor
#        Ryan Kethley
# Section:   565
# Assignment: 4.14 LAB: Make Change
# Date:  9/15/22

from math import *

A=int(input("Please enter the coefficient A: "))

if A<0:
    Asign="-"
else:
    Asign=""

Anum=abs(A)

if Anum==1:
   Anum="" 



B=int(input("Please enter the coefficient B: "))

if B<0:
    Bsign="-"
else:
    Bsign="+"
    
Bnum=abs(B)
if Bnum==1:
    Bnum=""
    



C=int(input("Please enter the coefficient C: "))

if C<0:
    Csign="-"
else:
    Csign="+"

Cnum=abs(C)




final=f"The quadratic equation is {Asign} {Anum}x^2 {Bsign} {Bnum}x {Csign} {Cnum} = 0"

if  A==0:
    final=final[:26]+final[30:]
    
    
if B==0:
    final=final[:31]+final[36:]
    
if C==0:
    final=final[:35]+final[39:]
   

print(final)
   

  