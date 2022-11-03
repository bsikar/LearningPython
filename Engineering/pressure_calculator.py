from math import log10
pressure=float(input('Pressure: '))
inverse=(1/pressure)
log=log10(pressure)

atm=pressure*0.00986923266
mmHg=pressure*7.50062

print(atm)
print(mmHg)