from Ex107 import moeda
num = int(input(f'Qual o valor da moeda? R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro (num, False)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade (num, True)}')
print(f'O aumento de 10% em {moeda.moeda(num)} é {moeda.aumentar(num,10, False)}')
print(f'A diminuição de 13% em {moeda.moeda(num)} é {moeda.diminuir(num,13, True)}')