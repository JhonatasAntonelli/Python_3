dados = dict()
jogador = str(input('Qual o nome do jogador? '))
todos = list()
gols_total = 0
gols_t = dict()
while jogador != '999':
    jogos = int(input(f'Quantos jogos o {jogador} jogou? '))
    dados ['jogador'] = jogador
    dados['jogos'] = jogos
    for c in range (1, jogos+1):
        gols = int(input(f'Quantos gols o {jogador} fez no {c}º jogo? '))
        gols_t[f'partida {c}'] = gols
        gols_total = gols_total + gols
    gols_t['Total de gols'] = gols_total
    todos.append(dados.copy())
    jogador = str(input('Qual o nome do jogador? (999 interrompe): '))
print (todos)
for e in todos:
    for c, v in e.items():
        print (f'{c} tem valor: {v} ')
print ('-='*30)
print ('Cod.'.ljust(10, ' '),  'Nome'.ljust(13, ' '), 'Gols'.ljust(13, ' '), 'Total'.ljust(15, ' '))
print ('-'*40)
for c in range (0, len(todos)):
    print(c, todos[c]['jogador'].ljust(10, ' '),end='')
    for k, v in c:
        print((v), end='')
    print(gols_t[c])
print ('-'*40)