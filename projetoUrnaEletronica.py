# Nomes: Felype Nunes RM: 96232 | Lais Leme RM: 94660

print('=-=' * 20)
cand1 = 'Joaquim Francisco'
cand2 = 'Miguel Arraes'
print(f'Candidato 1:{cand1}\nCandidato 2: {cand2}')
print('=-=' * 20)
votos = []
votosN = 0
voto1 = 0
voto2 = 0
x = 0
while x == 0:
    voto = int(input(f'Digite 1 para {cand1}, 2 para {cand2} \nou outro numero para voto nulo (digite 0 para encerrar a votação) : '))
    if voto != 0:
        votos.append(voto)
    elif voto == 0:
        print('=-=' * 20)
        print('Votação encerrada!')
        print(f'Os votos foram esses : {votos}.')
        print('=-=' * 20)
        voto1 = votos.count(1)
        voto2 = votos.count(2)
        for nulos in votos:
            if nulos != 1 and nulos != 2:
                votosN += 1
        eleitores = len(votos)
        print(f'A quantidade de votos do Candidato {cand1} foi: {voto1} sendo {voto1/eleitores*100:.2f}% dos votos')
        print(f'A quantidade de votos do Candidato {cand2} foi: {voto2} sendo {voto2/eleitores*100:.2f}% dos votos')
        print(f'A quantidade de votos nulos foi: {votosN} sendo {votosN/eleitores*100:.2f}% dos votos')
        print('=-=' * 20)
        x += 1