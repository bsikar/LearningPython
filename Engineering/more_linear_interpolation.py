# By submitting this assignment, I agree to the following: 
#  “Aggies do not lie, cheat, or steal, or tolerate those who do” 
#  “I have not given or received any unauthorized aid on this assignment” 
# 
# Name:   Evan Slyter
# Section:   565
# Assignment: more_linear_interpolation
# Date:  9/8/22




def interpolate(time,num,last):
    #datset 1
    t0=12 #seconds
    x0=8 #meters
    y0=6 #meters
    z0=7 #meters

    #dataset 2
    t2=85 #seconds
    x2=-5 #meters
    y2=30 #meters
    z2=9 #meters
    
    x1=x0+((x2-x0)/(t2-t0))*(time-t0)

    y1=y0+((y2-y0)/(t2-t0))*(time-t0)

    z1=z0+((z2-z0)/(t2-t0))*(time-t0)
    
    print(f"At time {time} seconds:\nx{num} = {x1} m\ny{num} = {y1} m \nz{num} = {z1} m\n")
    
    if last==False:
        print("-----------------------")
    
interpolate(30.0,1,0)

interpolate(37.5,2,0)

interpolate(45.0,3,0)

interpolate(52.5,4,0)

interpolate(60.0,5,1)