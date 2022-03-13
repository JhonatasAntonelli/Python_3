def leiapreço (msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" não é um preço invalido!')
        else:
            valido = True
            return float(entrada)
