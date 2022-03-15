def leiaint(msg):
    try:
        n = int(input('Digite um número inteiro: '))
    except(ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que você digitou')
        n = 'ERRO'
        return n
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os valores')
        n = 'ERRO'
        return n
    except Exception as erro:
        print(f'O erro encontrado foi {erro.__cause__}')
        n = 'ERRO'
        return n
    else:
        return n
def leiafloat(msg):
    try:
        f = float(input('Digite um número real: '))
    except(ValueError, TypeError):
        f = 'ERRO'
        print('Tivemos um problema com os tipos de dados que você digitou')
        return f
    except KeyboardInterrupt:
        print('O usuário preferiu não informar os valores')
        f = 'ERRO'
        return f
    except Exception as erro:
        print(f'O erro encontrado foi {erro.__cause__}')
        f = 'ERRO'
        return f
    else:
        return f
n = leiaint('Digite um número inteiro')
f = leiafloat('Digite um número real')
print(f'Os números que você digitou foram {n} e {f}')