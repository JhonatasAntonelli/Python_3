x = 0
a = int(input('Digite um número: '))
if a % 2 == 0:
    x = x +1
b = int(input('Digite um número: '))
if b % 2 == 0:
    x = x +1
c = int(input('Digite um número: '))
if c % 2 == 0:
    x = x +1
d = int(input('Digite um número: '))
if d % 2 == 0:
    x = x +1
e = int(input('Digite um número: '))
if e % 2 == 0:
    x = x +1
lista = (a, b, c, d, e)
if 9 in lista:
    print (lista.count(9))
else:
    print ('O valor 9 não foi digitado')
if 3 in lista:
    print (lista.index(3)+1)
else:
    print('O número 3 não foi digitado')
if x == 0:
    print('Não foi digitado nenhum número par')
else:
    print (f'Foi digitado {x} números pares')
y = []
z = 0
lista = ['a', 'b', 'c', 'd', 'e']
for x in lista:
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        z += 1
    y.append(x)
print (y.count(9))
print (y.index(3)+1)
print (z)