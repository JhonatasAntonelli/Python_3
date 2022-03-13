def metade(num = 0, formato = False):
    x = num/2
    return x if formato is False else moeda(x)


def dobro(num = 0, formato = False):
    x = num * 2
    return x if formato is False else moeda(x)


def diminuir(num = 0, p = 0, formato = False):
    x = num * ((100-p)/100)
    return x if formato is False else moeda(x)


def aumentar(num = 0,p = 0, formato = False):
    x = num * ((100+p)/100)
    return x if formato is False else moeda(x)


def moeda(num=0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num, a, d):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{a}% de aumento: \t{aumentar(num, a, True)}')
    print(f'{d}% de redução: \t{diminuir(num, d, True)}')
    print('-' * 30)