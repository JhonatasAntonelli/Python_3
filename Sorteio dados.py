from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
numero = int(input('Quantos jogadores? '))
for c in range (1,numero+1):
    jogo [f'{c}º jogador']= randint(1,6)
ranking = dict()
for k, v in jogo.items():
    print (f'O {k} tirou o valor {v} ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1))
print(ranking)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print (f'O {i+1}º lugar foi do {v[0]}, que tirou o valor {v[1]} ')
    sleep(1)