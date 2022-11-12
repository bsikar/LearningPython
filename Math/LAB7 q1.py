from sympy import *
from sympy.plotting import plot, plot_parametric

x = symbols("x")
f1 = 8 - (x**2)
f2 = 5 * (exp(-(((x - 2) / 2) ** 2)))
f11 = diff(f1, x)
f22 = diff(f2, x)

critf1 = solve(f11)
critf2 = solve(f22)


xvalues_list = []
xvalues_list = xvalues_list + critf1
xvalues_list = xvalues_list + critf2


lowerbound = -5
upperbound = 5

for index in range(len(xvalues_list)):
    if xvalues_list[index] < lowerbound or xvalues_list[index] > upperbound:
        xvalues_list.pop(index)

xvalues_list.append(lowerbound)
xvalues_list.append(upperbound)


if limit(f1, x, 0) != limit(f2, x, 0):
    xvalues_list.remove(0)

yvalues_list = xvalues_list[:]


for index in range(len(yvalues_list)):
    if yvalues_list[index] < 0:
        yvalues_list[index] = f1.subs(x, yvalues_list[index])
    elif yvalues_list[index] >= 0:
        yvalues_list[index] = f2.subs(x, yvalues_list[index])

absmax = max(yvalues_list)
absmin = min(yvalues_list)


xvalues_list = []
xvalues_list = xvalues_list + critf1
xvalues_list = xvalues_list + critf2

lowerbound = -10
upperbound = 10

for index in range(len(xvalues_list)):
    if xvalues_list[index] < lowerbound or xvalues_list[index] > upperbound:
        xvalues_list.pop(index)

xvalues_list.append(lowerbound)
xvalues_list.append(upperbound)


if limit(f1, x, 0) != limit(f2, x, 0):
    xvalues_list.remove(0)

yvalues_list = xvalues_list[:]

for index in range(len(yvalues_list)):
    if yvalues_list[index] < 0:
        yvalues_list[index] = f1.subs(x, yvalues_list[index])
    elif yvalues_list[index] >= 0:
        yvalues_list[index] = f2.subs(x, yvalues_list[index])

absmax = max(yvalues_list)
absmin = min(yvalues_list)

print(absmax)
print(absmin)
