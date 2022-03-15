try:
    a = int(input('Numerador: '))
    b = int(input('Denumerador: '))
    n = a/b
except(ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os valores')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {n:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
