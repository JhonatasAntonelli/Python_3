'''import random
import itertools
y = []
lista = ('a', 'b', 'c', 'd', 'e',)
for x in lista:
    x = random.randint(0, 150)
    y.append(x)
z = tuple(y)
z = sorted(z)
print (z[0])
print (z[-1])
print (z)
print (type(z))'''
import random
a = random.randint(0, 150)
b = random.randint(0, 150)
c = random.randint(0, 150)
d = random.randint(0, 150)
e = random.randint(0, 150)
x = (a, b, c, d, e)
print (x)
x = sorted(x)
print (x[0])
print (x[-1])

numeros = (random.randint(0, 150),random.randint(0, 150),random.randint(0, 150),random.randint(0, 150),random.randint(0, 150))
print (numeros)
numeros = sorted(numeros)
print (numeros[0])
print (numeros[-1])