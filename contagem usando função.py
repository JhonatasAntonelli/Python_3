import time
a = int(input('Digite o valor inicial: '))
def contagem (a, b, c):
    if a > b and c > 0:
        b = b - c
        c = c *(-1)
    else:
        b = b + 1
    print('-=-' * 10)
    print(f'Contegam de {a} até {b-1} de {c} em {c}')
    for x in range (a, b, c):
        print (x, end=' ')
        time.sleep(0.5)
    print('FIM!')
    print('-=-' * 10)
while a != 999:
    b = (int(input('Digite o valor final: ')))
    c = int(input('Digite o valor da sequência: '))
    contagem(a, b, c)
    print ()
    a = int(input('Digite o valor inicial: (999 interrompe): '))