nome_peso = list ()
dados = list ()
continuar = 's'
while continuar == 's':
    nome_peso.append(str(input('Digite o seu nome: ')))
    nome_peso.append(int(input('Digite o seu peso: ')))
    dados.append(nome_peso[:])
    nome_peso.clear()
    continuar = str(input('Deseja continuar (S/N)')).lower()
print(len(dados))
dado = sorted(dados, key=lambda dados: dados[1])
print (dado)

print (f'As pessoal mais leves são {dado[0][0], dado [1][0], dado [2][0]}')
print (f'As pessoal mais pesadas são {dado[-1][0], dado [-2][0], dado [-3][0]}')




