def mostralinha():  #todas as funções tem () no final
    print('-'*50)


mostralinha()
print('Sistema de alunos')
mostralinha()
def mensagem(msg):
    print('-'*50)
    print(msg)
    print('-'*50)
mensagem('Sistema de alunos')
mensagem('CURSO EM VIDEO')

def soma(a,b):
    print(f'A igual a {a} e B igual a {b}')
    s = a + b
    print(f'A soma de {a} e {b} é {s}')


soma(4,5)
soma(b = 4, a = 9)
soma(a = 2, b = 1)


def contador (*num):#nesse caso ele cria uma tupla com os valores
    for c in num:
        print(f'{c}', end=', ')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

contador (2,1,7)
contador (2,7,8,4,5,6,9)


def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
valores = [2,5,7,4,9,8,6]
dobra(valores)
print(valores)


def somar (*valores):
    s = 0
    for numeros in valores:
        s += numeros
    print(f'A soma dos números {valores} é {s}')
somar (2,5,8,7,)
somar (3,5,4)