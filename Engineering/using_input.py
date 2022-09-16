# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: 3.17 LAB: Using input
# Date:  9/15/22

import math

#force
print("This program calculates the applied force given mass and acceleration")
mass=float(input("Please enter the mass (kg): "))

acceleration=float(input("Please enter the acceleration (m/s^2): "))

force=mass*acceleration
print(f"Force is {force:.1f} N")

#wavelength
print("This program calculates the wavelength given distance and angle")
distance=float(input("Please enter the distance (nm): "))
angle=float(input("Please enter the angle (degrees): "))
wavelength=(2*distance)*math.sin(math.radians(angle))
print(f"Wavelength is {wavelength:.4f} nm")

#radon
print("This program calculates how much Radon-222 is left given time and initial amount")
time=float(input("Please enter the time (days): "))
initialAmt=float(input("Please enter the initial amount (g): "))
halfLife=3.8

howMuch=(2**((-1*time)/halfLife)*initialAmt)
print(f"Radon-222 left is {howMuch:.2f} g")

#pressure
print("This program calculates the pressure given moles, volume, and temperature")
moles=float(input("Please enter the number of moles: "))
volume=float(input("Please enter the volume (m^3): "))
temperature=float(input("Please enter the temperature (K): "))
pressure=((moles)*(8.314)*(temperature))/volume
pressure/=1000
print(f"Pressure is {round(pressure)} kPa")