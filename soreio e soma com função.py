numeros = list()
import random
def soreteia(numeros):
    num = 0
    for c in range (0,5):
        num = random.randint(0,20)
        numeros.append(num)
    print(numeros)
def somapar(numeros):
    soma = 0
    for c in numeros:
        if (c % 2) == 0:
            soma += c
    print(soma)
soreteia(numeros)
somapar(numeros)


