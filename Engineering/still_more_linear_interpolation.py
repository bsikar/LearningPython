# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Names: Evan Slyter
#        Sam Kinnard
#        Caleb Lorimor
#        Ryan Kethley

# Section:   565
# Assignment: 3.16 LAB: Still more Linear Interpolation
# Date:  9/8/22

#first set of inputs
t0=float(input("Enter time 1:"))
x0=float(input("Enter the x position of the object at time 1:"))
y0=float(input("Enter the y position of the object at time 1:"))
z0=float(input("Enter the z position of the object at time 1:"))

#second set of inputs
t2=float(input("Enter time 2:"))
x2=float(input("Enter the x position of the object at time 2:"))
y2=float(input("Enter the y position of the object at time 2:"))
z2=float(input("Enter the z position of the object at time 2:"))





def interpolate(t0,x0,y0,z0,t2,x2,y2,z2):
    
    #Splits time into four even chunks
    interval=(t2-t0)/4
    
    time=t0
    x1=x0+((x2-x0)/(t2-t0))*(time-t0)
    y1=y0+((y2-y0)/(t2-t0))*(time-t0)
    z1=z0+((z2-z0)/(t2-t0))*(time-t0)
    
    print(f"At time {time:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")
    
    time+=interval
    x1=x0+((x2-x0)/(t2-t0))*(time-t0)
    y1=y0+((y2-y0)/(t2-t0))*(time-t0)
    z1=z0+((z2-z0)/(t2-t0))*(time-t0)
    print(f"At time {time:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

    time+=interval
    x1=x0+((x2-x0)/(t2-t0))*(time-t0)
    y1=y0+((y2-y0)/(t2-t0))*(time-t0)
    z1=z0+((z2-z0)/(t2-t0))*(time-t0)
    print(f"At time {time:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")
    
    time+=interval
    x1=x0+((x2-x0)/(t2-t0))*(time-t0)
    y1=y0+((y2-y0)/(t2-t0))*(time-t0)
    z1=z0+((z2-z0)/(t2-t0))*(time-t0)
    print(f"At time {time:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")
    
    time+=interval
    x1=x0+((x2-x0)/(t2-t0))*(time-t0)
    y1=y0+((y2-y0)/(t2-t0))*(time-t0)
    z1=z0+((z2-z0)/(t2-t0))*(time-t0)
    print(f"At time {time:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")
    
interpolate(t0,x0,y0,z0,t2,x2,y2,z2)
