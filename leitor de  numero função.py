def leiaint(msn):
    while True:
        n = str(input(msn))
        if n.isnumeric():
            break
        else:
            print(f"\033[1;31m"'ERRO! digite um número inteiro válido'"\033[0;0m")
    return n
n = leiaint('Digite um número: ')
print(f'O número que você digitou foi {n}')


