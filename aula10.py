# exercicio 1
depositoInicial = float(input("Qual foi o seu deposito inicial R$"))
taxaJuros = float(input("Qual sua taxa de Juros (%) :"))
contadora = 1
saldo = depositoInicial

while contadora <= 24:
    saldo = saldo + saldo * (taxaJuros / 100)
    print(f"Saldo do mês {contadora} R${saldo:.2f}")
    contadora += 1

print(f"O ganho total foi R${saldo:.2f}")

# exercicio 2

depositoInicial1 = float(input("Qual foi o seu deposito inicial R$"))
taxaJuros1 = float(input("Qual sua taxa de Juros (%) :"))
contadora1 = 1
saldo1 = depositoInicial
saldoMensal = float(input("Qual o valor mensal que você ira colocar por mês R$"))

while contadora1 <= 24:
    saldo1 = saldoMensal + saldo1 + saldo1 * (taxaJuros1 / 100)
    print(f"Saldo do mês {contadora1} R${saldo1:.2f}")
    contadora1 += 1

print(f"O ganho total foi R${saldo1:.2f}")

# exercicio 3

soma = 0
while True:
    num = int(input("Digite um numero para somar ou 0 para sair: "))
    if num == 0:
        break
    soma += num
    print("Soma =", soma)

# exercicio 4

notas = [6, 7, 5, 8, 9]
soma = 0
x = 0

while x < 5:
    soma += notas[x]
    x += 1
print(f"Médía = {(soma / x):.2f}")

#exercicio 5

notas = [0,0,0,0,0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input(f"Nota{x+1} = "))
    soma += notas[x]
    x += 1
print(f"Médía = {(soma/x):.2f}")