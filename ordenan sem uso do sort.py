numero = int(input('Digite um número: '))
lista = []
lista.append(numero)
continuar = 's'
while continuar == 's':
    numero = int(input('Digite um número: '))
    y = 0
    x = 0
    while y != 1:
        if numero == lista [x]:
            lista.insert(x, numero)
            y += 1
        if numero < lista [x]:
            lista.insert(x,numero)
            y +=1
        if numero > lista [-1]:
            lista.append(numero)
            y += 1
        x += 1
    continuar = input('Quer continuar S/N: ').lower()
    while continuar.isnumeric():
        continuar = str(input('Quer continuar S/N: ')).lower()
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar S/N: ')).lower()
    continuar = str(continuar)
print (lista)