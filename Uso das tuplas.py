lanches = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanches[1])
print(lanches[1:])
print(lanches[:2])
print(len(lanches))
for comida in lanches:# O uso do for faz com que seja aplicado um elemento da tupla por vez e quando os elemento acabarem o programa sai do for
    print(f'Eu vou comer {comida}')#atribui o elemento em lanches no nome comida e depois atribui no proximo elemento
print('Comi pra caramba')
for cont in range (0, len(lanches)):#para cont no intervalo de 0 até o comprimento,
    print(lanches[cont]) #imprima lanche no local cont
for pos,  comida in enumerate(lanches):# com a função enumerate é possível colocar 1º a posição do objeto e 2º o nome do objeto
    print (f'Eu vou comer {comida}, na posição {pos}')
print(sorted(lanches))# sorted organiza a lista
a = (1,2,3,4)
b = (2,5,6,7)
c = a + b
print (c)
print(c.count(2)) #A função count mostra quantas vezes o elentento aparece na tupla
print(c.index(5))# A função index mostra o local em que se encontra o objeto
print(c.index(2,3))#Quando é colocado um segundo elemento, esse indica o local que devemos começar a olhar
del lanches
print (lanches)