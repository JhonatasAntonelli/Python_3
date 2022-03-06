numero = int(input('Digite um número: '))
lista = []
while numero != 0:
    numero = int(input('Digite um número, para encerrar a lista, digite 0: '))
    if numero != 0:
        lista.append(numero)
x = y = lista [0]
for c, v in enumerate(lista):
    if lista [c] > x:
        x = lista [c]
    if lista [c] < y:
        y = lista [c]
z = lista.index(y)
d = z + 1
print(f'O menor número é o {y}',end=' ')
print (f'na posição {z}...', end=' ')
while y in lista [d:]:
    a = lista.index(y,d)
    print(f'{a}...', end= '')
    d += 1
w = lista.index(x)
e = w + 1
print(f'\nO maior número é o {x}',end=' ')
print (f'na posição {w}...', end=' ')
while x in lista [e:]:
    b = lista.index(x,e)
    print(f'{b}...')
    e += 1
