def ficha (n = '<Desconhecido>', g = 0):
    print(f'O jogador {n} fez {g} gol(s)')
nome = str(input('Qual o nome do jogador? '))
gols = input(f'Quantos gols o jogador {nome} fez? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(g = gols)
else:
    ficha(nome, gols)