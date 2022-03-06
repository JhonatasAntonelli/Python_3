import time
valores = list()
quantidade = int(input('Quantos números você quer na sequência: '))
continuar = 'S'
def maior(*numeros):
    print('-=-' * 10)
    time.sleep(1)
    valores.sort()
    print(f'Foram informados {quantidade} valores valores ao todo, sendo eles {valores}')
    time.sleep(2)
    print(f'O maior vlor informado foi {valores[-1]}')
    print('-=-' * 10)
while continuar == 'S':
    for c in range(0,quantidade):
        valores.append(int(input(f'Digite o {c+1}º número: ')))
        maior()
    continuar = str(input('Deseja continuar? (S/N): ')).upper()