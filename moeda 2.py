import moeda
num = int(input('Qual o valor da moeda? R$ '))
print(f'O dobro de R$ {num} é R$ {moeda.dobro(num)}')
print(f'A metade de R$ {num} é R$ {moeda.metade(num)}')
print(f'O aumento de 10% em R$ {num} é R$ {moeda.aumentar(num,10)}')
print(f'A diminuição de 13% em R$ {num} é R$ {moeda.diminuir(num,13)}')