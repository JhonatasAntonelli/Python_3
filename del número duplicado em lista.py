numero = int(input('Digite um número: '))
lista = []
lista.append(numero)
continuar = 's'
while continuar == 's':
    numero = int(input('Digite um número: '))
    if numero in lista:
        numero = numero
        print ('Esse número já foi adicionado anteriormente')
        continuar = input('Quer continuar S/N: ').lower()
        while continuar.isnumeric():
            continuar = str(input('Quer continuar S/N: ')).lower()
        while continuar != 's' and continuar !='n':
            continuar = str(input('Quer continuar S/N: ')).lower()
        continuar = str(continuar)
    else:
        lista.append(numero)
        print ('Valor adicionado com sucesso!')
        continuar = input('Quer continuar S/N: ').lower()
        while continuar.isnumeric():
            continuar = str(input('Quer continuar S/N: ')).lower()
        while continuar != 's' and continuar !='n':
            continuar = str(input('Quer continuar S/N: ')).lower()
        continuar = str(continuar)
lista.sort()
print(f'Os número adicionados na lista são {lista}')