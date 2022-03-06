galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]#com  o [0] pega apenas a primeira letra
        if pessoas['sexo'] in 'MF':# se tiver M ou F em sexo ele para
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoas ['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resposta == 'N':
        break
print (f'Ao todo temoos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print (f'A media de idade é de {media:5.2f} anos')# 5 casas ao todo e 2 decimais
print ('As mulhers cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('Lista de pessoas acima da média: ')
for p in galera:
    if p ['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
            print ()
print('ENCERRADO')
