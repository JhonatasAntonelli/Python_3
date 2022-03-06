par = list ()
impar = list ()
continuar = 's'
while continuar == 's':
    numero = (int(input('Digite um numero: ')))
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 != 0:
        impar.append(numero)
    continuar = str(input('Deseja continuar (S/N)')).lower()
print (f'Os números paraes são: {sorted(par)}')
print (f'Os números impares são: {sorted(impar)}')
