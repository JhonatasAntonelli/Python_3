dados = dict()
lista = list()
lista_mulheres = list()
lista_media = list()
idades = list()
nome = str(input('Qual o nome da pessoa?(999 interrompe): '))
numero = 0
idade_total = 0
while nome != '999':
    idade = int(input(f'Qual a idade do {nome}? '))
    idades.append(idade)
    idades.append(nome)
    idade_total = idade + idade_total
    sexo = str(input(f'Qual o sexo do {nome} (M/F)? ').upper())
    idades.append(sexo)
    if sexo == 'F':
       lista_mulheres.append(nome)
    numero += 1
    dados ['nome'] = nome
    dados ['idade'] = idade
    dados ['sexo'] = sexo
    lista.append(dados.copy())
    nome = str(input('Qual o nome da pessoa?(999 interrompe): '))
media = idade_total/numero
x = 0
y = 1
z = 2
print(f'As mulheres cadastradas são {lista_mulheres}')
print(f'A média de idade é {media}')
print(f'Foram cadastradas {numero} pessoas')
print (f'As pessoal com idade acima da média são {lista_media}')
while y < len(idades):
    if idades [x] > media:
        print (f'nome = {idades[y]}; Sexo {idades [z]}; Idade = {idades [x]}')
    x += 3
    y += 3
    z += 3