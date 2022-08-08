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

def pedirNota():
    x = float(input("Digite a nota: "))
    return x

# ======== /\ funções =========== \/ codigo ==========

print(f"============== Calcule o primeiro semestre ================")
print("---------------- Digite as 3 notas dos CheckPoints ------------------")
ch1 = pedirNota()
ch2 = pedirNota()
ch3 = pedirNota()

ch0 = checkpoint(ch1,ch2,ch3)
print("=================================================================")
print("---------------- Digite as 2 notas das Sprints ------------------")
sp1 = pedirNota()
sp2 = pedirNota()

sp0 = Sprint(sp1,sp2)
print("=================================================================")
print("---------------- Digite a nota do Global Solution ------------------")
md1 = pedirNota()

md0 = totalGlobal(md1, sp0, ch0 )
print("=================================================================")
print(f"---------------- Sua media no primeiro semestre é {md0} ------------------")

print("=================================================================")
print(f"================== Calcule o segundo semestre ====================")
print("---------------- Digite as 3 notas dos CheckPoints ------------------")
ch1_1 = pedirNota()
ch2_1 = pedirNota()
ch3_1 = pedirNota()

ch0_1 = checkpoint(ch1_1,ch2_1,ch3_1)

print("=================================================================")
print("---------------- Digite as 2 notas das Sprints ------------------")
sp1_1 = pedirNota()
sp2_1 = pedirNota()

sp0_1 = Sprint(sp1_1,sp2_1)

print("=================================================================")
print("---------------- Digite a nota do Global Solution ------------------")
md1_1 = pedirNota()

md0_1 = totalGlobal(md1_1, sp0_1, ch0_1 )

print("=================================================================")
print(f"---------------- Sua media no segundo semestre é {md0_1} ------------------")

n = ((md0*0.4)+(md0_1*0.6))

if n >= 60:
    print("=================================================================")
    print(f"       Parabéns você foi aprovado, sua media final é {n}  =)")
    print("=================================================================")
elif n >= 40:
    print("Você tera que realizar outro exame para conseguir passar de ano")
    novaNota = float(input("Qual nota você conseguiu nesse exame ?"))
    if novaNota >= 60:
        print("=================================================================")
        print("                Parabéns você conseguiu passar! =)")
        print("=================================================================")
    else:
        print("=================================================================")
        print("               Infelizmente você não conseguiu passar! =(")
        print("=================================================================")
else:
    print("=================================================================")
    print("               Infelizmente você não foi aprovado =(")
    print("=================================================================")


