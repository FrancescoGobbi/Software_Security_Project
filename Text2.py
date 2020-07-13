#Text2.py

def Pippo(casa):
    if casa>=10:
        x = 20
    else:
        x = 30
    
    return x


aliquota = [15000.0, 28000.0, 55000.0, 75000.0, 75000.0]
percentuale = [0.23,0.27,0.38,0.41,0.43]
eccesso = [0, 3450.0, 6960.0, 17220.0, 25420.0 ]

def irpef_calculation(income):
    i = 0
    for i in range(0,5):
        if (income < (aliquota[i])):
            irpef = income * percentuale[i]
            return irpef
        if (i == 4 and income>aliquota[i]):
            irpef = eccesso[i] + (income-aliquota[i])*percentuale[i]
            return irpef
        if (income>aliquota[i] and income<=aliquota[i+1]):
            irpef = eccesso[i+1] + (income-aliquota[i])*percentuale[i+1]
            return irpef

        

x = aliquota[2] * percentuale[3]
print(x)
irpef = irpef_calculation(12000)
print(irpef)