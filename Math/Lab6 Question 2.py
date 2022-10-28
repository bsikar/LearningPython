from sympy import *
from sympy.plotting import (plot,plot_parametric)
x,y=symbols('x y')
eqn = (-((x**2+y**2)/4)+2*x-2)**2 - 5*(x**2+y**2)
pcurve=plot_implicit(eqn,(x,-5,20),(y,-15,15),show=False)


x,y=symbols('x y')
eqn = (-((x**2+y**2)/4)+2*x-2)**2 - 5*(x**2+y**2)
dydx=idiff(eqn,y,x)
print('Implicit differentiation yields dy/dx=',dydx)

x,y=symbols('x y')

#NUM=numer(dydx)
#htan=solve([NUM,eqn],[x,y])
#print('Horizontal tangents at',htan)

DEN=denom(dydx)
vtan=solve([DEN,eqn],[x,y])
print('Vertical tangents at',vtan)
print("Hi")

x,y=symbols('x y')

pcurve=plot_implicit(eqn,(x,-2.5,2.5),(y,-2.5,2.5),show=False)

t=symbols('t')
phoriz=plot_parametric((t,-2,(t,-2.5,2.5)),(t,2,(t,-2.5,2.5)),show=False)

pvert=plot_parametric((-2,t,(t,-2.5,2.5)),(2,t,(t,-2.5,2.5)),show=False)
pcurve.extend(phoriz)
pcurve.extend(pvert)
pcurve.show()
