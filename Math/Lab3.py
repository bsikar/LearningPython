from sympy import *
from math import *
from sympy.plotting import (plot,plot_parametric)

#1a
#result from sympy import *
x = symbols('x')
f = x**5 + (4*x**3) - (2*(x**2)) + (8*x) - 1
print(f'Since f(0) = -1 and f(1) = 10, using the Interval Value Theorem we can conclude that there exists a value "c" between x = 0 and x = 1, where, f(c) = 0')
#1b
x = symbols('x')
f = x**5 + (4*x**3) - (2*(x**2)) + (8*x) - 1
print(nsolve(f,x,0))


#2a
x = symbols('x')
f1 = 2*x-3
f2 = 4*x-x**2
f3 = (x**2-6*x+8)/(x-4)
f4 = E**((x-4)*ln(3))
left3 = limit(f1,x,3)
right3 = limit(f2,x,3)
left4 = limit(f2,x,4)
right4 = limit(f3,x,4)
left5 = limit(f3,x,5)
right5 = limit(f4,x,5)
print(left3, right3, left4, right4, left5, right5)
print("The function is not continous at x = 4 (left contious). All other points are contious")
#2b
plot((f1,(x,0,3)),(f2,(x,3,4),f3,(x,4,5),f4,(x,5,oo)))


#3a

K = 1000
P = 10
r = 0.1
t = symbols('t')
Pt = (K * P)/ (P + (K - P) * (E ** (-1 * (r) * (t))))
L = limit(Pt, t, oo)
print(L)
plot(Pt) #NOT SURE IF THIS RIGHT


#3b

K = 1
P = 10
r = 0.1
t = symbols('t')
Pt = (K * P)/ (P + (K - P) * (E ** (-1 * (r) * (t))))
L = limit(Pt, t, oo)
print(L)
plot(Pt) #NOT SURE IF THIS IS RIGHT


#3c
growthRate=0.1
startingAmount=10
time=symbols('t')
k=15
f1=(k*startingAmount)/(startingAmount+(k-startingAmount)*(E**(-1*growthRate*time)))

print(limit(f1,time,oo))
plot(f1) #NOT SURE IF THIS IS RIGHT
