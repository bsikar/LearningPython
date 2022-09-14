# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: 1.11 LAB: Print math
# Date:  8/30/22

import math

#force
acceleration=5.5
mass=3
force=mass*acceleration
print("Force is "+str(force)+" N")

#wavelength
distance=0.025
angle=25
wavelength=(2*distance)*math.sin(math.radians(angle))
print("Wavelength is "+str(wavelength)+" nm")

#radon
initialAmt=5
halfLife=3.8
time=3

howMuch=(2**((-1*time)/halfLife)*initialAmt)
print("Radon-222 left is "+str(howMuch)+" g")

#pressure
volume=0.25
moles=5
temperature=415
pressure=((moles)*(8.314)*(temperature))/volume
pressure/=1000
print("Pressure is "+str(pressure)+" kPa")

