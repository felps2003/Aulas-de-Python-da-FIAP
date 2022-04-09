#Listas

print("======== Exercicio 0 ===========")
#Criando Listas
lista = [0,1,2,3]

print(lista)
print(lista[1])
print(lista[2])
print(lista[3])

print("======== Exercicio 1 =========")
#mudando variaveis dentro das listas

z = [4,6,3]

print(z)
z[0] = 2
print(z[0])

print("======== Exercicio 2 =========")
#calculando Notas Aritmeticas

notas=[6,7,5,8,9]
soma=0
x=0

while x < 5:
    soma += notas[x]
    x += 1
print(f"Média = {(soma/x):.2f}")

print("======== Exercicio 3 =========")
#calculando Notas Aritmeticas (vendo uma a uma)

nota=[0,0,0,0,0]
somas=0
x1=0

while x1 < 5:
    nota[x1] = float(input(f"Nota {x1+1} ="))
    somas += nota[x1]
    x1 += 1
print(f"Média = {(somas/x1):.2f}")

print("======== Exercicio 4 =======")
#Copia e fatiamento de lista (Quando copiamos uma lista para outra varivel, se alterarmo também alterara a lista original)
L = [1, 2, 3, 4, 5]
V = L
print(L)
print(V)
V[0] = 6
print(V)
print(L)

print("======== Exercicio 5 ======")
#Lista e suas formas de serem apresentadas
L1=[1,2,3,4,5]
print(L1[0:5])
print(L1[:5])
print(L1[:-1])
print(L1[1:3])
print(L1[1:4])
print(L1[3:])
print(L1[:3])
print(L1[-1])
print(L1[-2])


print("======== Exercicio 5 =========")
#Utilizando a função (len)

L = [12,9,5]
print(len(L))
V = []
print(len(V))

print("-----------------")

l = [1,2,3]
x3 = 0
while x3 < len(l):
    print(l[x3])
    x3 += 1


print("======= Exercicio 6 =========")
#Utilizando a função append para adicionar novas variaveis na lista

lista6 = []
lista6.append("a")
lista6.append("b")
lista6.append("c")
print(lista6)
print(len(lista6))


print("======== Exercicio 7 ========")

lista7 = []
while True:
    num = int(input("Digite um número (0 sai): "))
    if num == 0:
        break
    lista7.append(num)
x = 0
while x < len(lista7):
    print(lista7[x])
    x += 1

print("======== Exercicio 8 ========")
#Outra forma de  adicionar mais variaveis na lista é com o simbolo (+)

lista8 = []
lista8 = lista8 + [1]
print (lista8)
lista8 += [2]
print(lista8)
lista8 += [3,4,5]
print(lista8)

print("=========== Exercicio 9 ===========")
#utilizando o metodo extends e o metodo append

lista9 =[]
lista9.extend(["a", "b"])
print(lista9)
lista9.append(["c", "d"])
print(lista9)
print(len(lista9))
print(lista9[0])
print(lista9[1])
print(lista9[2])

print("========= Exercicio 10 ===========")
#Aprendendo a remover elementos da lista com a função (del)

lista10 = ["a", "b", "c"]
print(lista10)
del lista10[1]
print(lista10)

print("--------------")

lista10_1 = [1,2,3,4,5,6,7,8,9,10]
print(lista10_1)
del lista10_1[0:3]
print(lista10_1)

print("============ Exercicio 11 ==========")
lista11 =  [15,7,27,39]
pesquisa = int(input("Digite o valor a pesquisar:"))
x11 = 0

while x11 < len(lista11):
    if lista11[x11] == pesquisa:
        achou = True
        break
    else:
        achou = False
        break
    x += 1
if achou == True:
    print(f"{pesquisa} achado na posição {x11}.")
else:
    print(f"{pesquisa} não encontrado")
