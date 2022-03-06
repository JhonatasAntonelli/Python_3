lista = list()
lista.append('Pedro')
lista.append(25)
lista_lista = list()
lista_lista.append(lista[:])#adicionei uma copia da lista no lista_lista
lista [0] = 'Maria' #na lista foi trocado, mas não na lista_lista, pois la eu tenho uma copis
lista [1] = 32
lista_lista.append(lista[:])
print (lista_lista)
galera = [['joao', 18], ['Maria', 19], ['Pedro', 20], ['Lucas', 21]]#As listas devem ser separadas por virgula
print (galera[0])
print (galera[0][0])
for pessoa in galera:
    print (pessoa)
    print(pessoa[0])
    print (f'{pessoa[0]} tem {pessoa[1]} anos de idade')
grupo = list()
dados = list()
for c in range (0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('idade: ')))
    grupo.append(dados[:])#não pode esquecer de copiar a copia dos dados
    dados.clear()#cleaar apaga a lista
print (grupo)
for p in grupo:
    if p[1] >= 18:
        print (f'{p[0]} é maior de idade')
    else:
        print (f'{p[0]} é menor de idade')