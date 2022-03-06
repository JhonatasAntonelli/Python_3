def notas(*n, sit=False):
    """ As [] adicionam um parametro no dicionário 'r'
    e o  False ou True vão mostrar o parametro sit
    Isso ocorre com qualquer parametro da função"""
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        if r['média'] >= 5:
            r['situação'] = 'Regular'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
