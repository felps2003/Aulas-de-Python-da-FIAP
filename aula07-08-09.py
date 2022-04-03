#Aula que ensina como utilizar looping  no python com (while)


#exercicio 1
x = 1
while x <= 100:
    print(x)
    x += 1

print("-----------------")
#exercicio 1
y = 50
while y <= 100:
        print(y)
        y += 1

print("-----------------")
#exercicio 3
z = 10
while z >= 0:
    print(z)
    z -= 1

else:
    print("fogo")

print("-----------------")
#exercicio 4
fim = int(input("Qual deve ser o fim da contagem?"))
x = 1
while x <= fim:
    print(x)
    x += 1

print("-----------------")
#exercicio 5

x = 3

while x <= 30:
    print(x)
    x = x+3

print("-----------------")
#exercicio 5

x = 1
num = 2
while x <=10 :
    print(num,"x",x,"=",num*x)
    x += 1

print("-----------------")
#exercicio 5
num = int(input("Qual tabuada:"))
inicio = int(input("Qual sera o primeiro multiplicador da tabuada:"))
fim = int(input("Qual sera o ultimo multiplicador da tabuada:"))
x = 1
while inicio <= fim :
    print(num,"x",inicio,"=",num*inicio)
    inicio += 1
