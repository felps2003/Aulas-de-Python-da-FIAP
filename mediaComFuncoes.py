def checkpoint(num1, num2, num3):
    numAux = 0.0
    if num1 < num2:
        numAux = num1
    else:
        numAux = num2
    if num3 < numAux:
        numAux = num3
    return ((num1+num2+num3)-numAux)/2

def Sprint(num1,num2):
    return (num1+num2)/2

def totalGlobal(gs, sp, ch):
    return (ch*0.4)+(sp*0.4)+(gs*0.6)

def notaFinal(med1, med2):
    return (med1*0.4)+(med2*0.6)

ch1 = checkpoint(50.0,50.0,20.0)
sp1 = Sprint(70.0,90.0)
md1 = totalGlobal(100.0, sp1, ch1 )

ch2 = checkpoint(50.0,50.0,20.0)
sp2 = Sprint(70.0,90.0)
md2 = totalGlobal(50.0, sp1, ch1 )

print(f"Sua nota final é: {notaFinal(md1,md2)}")



