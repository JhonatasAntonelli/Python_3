import random
import time
aposta = list()
jogos = int(input('Quantos cartões você quer jogar? '))
numeros = int(input('Quantos números você quer em cada jogo? '))
print ('As apostas são:')
x = 1
for a in range(0, jogos):
    for c in range(0,numeros):
        numero = random.randint(1,60)
        while numero in aposta:
            numero = random.randint(1,60)
        aposta.append(numero)
    print (f'Jogo {x} {sorted(aposta)}')
    time.sleep(1)
    aposta.clear()
    x += 1
