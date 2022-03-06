dados = dict() #cria um dicionário
dados = {'nome': 'Pedro', 'idade': 25}# também pode ser criado abrindo e fechando chaves
print (dados['idade'])
print (dados['nome'])
dados['sexo']= 'M' # para adicionar um elemento, como o nome sexo ainda não existe ele vai criar esse elemento
del dados['idade']# vai apagar um elemento
print (dados['sexo'])
print(dados.values())#vai apresentar todos os valores
print(dados.keys())# vai mostrar as chaves
print(dados.items())# vai mostrar tudo
for k,v in dados.items():
    print(f'O {k} é {v}')
# é possivel criar uma lista de dicionários adicionando-os na lista
# Ex: print(locadora[0]['ano']) vai imprimir o ano do elemento zero da lista
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print (f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
for k in pessoas:
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')
estado1 = {'uf':'São Paulo', 'sigla':'SP'}
estado2 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
estado = dict()
pais = list()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    pais.append(estado.copy())
print (pais)
for e in pais:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')