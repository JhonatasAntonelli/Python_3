def validacao(x, msg, tipo):
    while True:
        try:
            tipo (x)
        except(ValueError, TypeError):
            print('Tivemos um problema com os tipos de dados que você digitou')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os valores')
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
        else:
            return x
            break
        x = input(f'Digite um número {msg}: ').replace(',', '.').strip()
n = validacao((input('Digite um número inteiro: ')), 'inteiro', int).strip()
r = validacao((input('Digite um número real: ')).replace(',', '.').strip(), 'real', float)
print(f'Você digitou os números {n} e {r}')