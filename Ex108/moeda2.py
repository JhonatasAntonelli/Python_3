from Ex107 import moeda
num = float(input(f'Qual o valor da moeda? R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O aumento de 10% em {moeda.moeda(num)} é {moeda.moeda(moeda.aumentar(num,10))}')
print(f'A diminuição de 13% em {moeda.moeda(num)} é {moeda.moeda(moeda.diminuir(num,13))}')