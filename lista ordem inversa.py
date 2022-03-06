lista = []
continuar = 's'
while continuar == 's':
    numero = input('Digite um número: ')
    while numero.isalpha():
        numero = input('Digite um número: ')
    if numero.isnumeric():
        numero = int(numero)
        lista.append(numero)
    continuar = input('Quer continuar S/N: ').lower()
    while continuar.isnumeric():
        continuar = str(input('Quer continuar S/N: ')).lower()
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar S/N: ')).lower()
    continuar = str(continuar)
x = len(lista)
lista.sort(reverse=True)
print (f'você digitou {x} elementos')
print ('A lista em ordem decrescente é', lista)
if 5 in lista:
    print('O valor 5 está na posição', lista.index(5)+1)
else:
    print('O 5 não foi encontrado na lista')