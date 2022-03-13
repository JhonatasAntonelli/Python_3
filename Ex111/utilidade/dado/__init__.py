def leiapreço (msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isnumeric():
            valido = True
            return float(entrada)
        else:
            print(f'ERRO: \"{entrada}\" não é um preço invalido!')

