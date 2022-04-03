#Aprendendo a Utilizar if , elif e else

#exemplo1
idade = int(input("Quantos anos você tem?"))

if idade >= 18:
    print("você é maior de idade")
else:
    print("Você é menor de idade")

#exemplo2
minutos = int(input("Quantos minutos você utilizou neste mês: "))
if minutos < 200:
    preco = 0.2*minutos
else:
    if minutos <= 400:
        preco = 0.18*minutos
    else:
        preco = 0.15*minutos
print("Você vai pagar este mês R$ %.2f"%preco)