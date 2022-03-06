lista = ['pizza', 'suco', 'hamburguer', 'churrasco']
print (lista)
lista.append('sorvete')
print (lista)
lista.insert(2, 'brigadeiro')#insert insere um objeto na lista em um local determinado
print (lista)
del lista[3]#apaga no local indicado
print (lista)
lista.pop(3)#apaga = o del
print (lista)
lista.pop()# apaga o ultimo elemento
print (lista)
if 'pizza' in lista:
    lista.remove('pizza')# remove o objeto, não é necessário colocar o if, apeas se não tiver certeza que o objeto está na lista
print (lista)
valores = list(range(4,11))
print (valores)
valores.sort(reverse=True)
for v in valores:
    #print (f'{v}...', end=' ')
    print(f'{v}...')
for c, v in enumerate(valores):
    print (f'Na posição {c+1} encontrei {v}')
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print (valores)
a = valores #Assim estamos nos referindo a mesma lista, aterando uma, altera a outra igualmente
a = valores [:]#Assim criamos uma nova lista sem ligação com a anterior
