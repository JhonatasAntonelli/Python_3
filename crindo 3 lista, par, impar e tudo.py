lista = []
lista_par = []
lista_impar = []
continuar = 's'
while continuar == 's':
    numero = input('Digite um número: ')
    while numero.isalpha():
        numero = input('Digite um número: ')
    if numero.isnumeric():
        numero = int(numero)
        lista.append(numero)
        if numero % 2 == 0:
            lista_par.append(numero)
        if numero % 2 != 0:
            lista_impar.append(numero)
    continuar = input('Quer continuar S/N: ').lower()
    while continuar.isnumeric():
        continuar = str(input('Quer continuar S/N: ')).lower()
    while continuar != 's' and continuar != 'n':
        continuar = str(input('Quer continuar S/N: ')).lower()
    continuar = str(continuar)

print (f'os números digitados foram {lista}')
print (f'Os números pares são {lista_par}')
print (f'Os números impares são {lista_impar}')
