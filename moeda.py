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