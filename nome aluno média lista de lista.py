lista = list()
media = list()
listas = list()
aluno = str(input('Digite o nome do aluno: '))
numero = 0
individual = 'Jhonatas'
while aluno != '999':
    lista.append(str(numero))
    lista.append(aluno)
    media.append(aluno)
    nota_1 = int(input('Digite a primeira nota do aluno: '))
    lista.append(nota_1)
    nota_2 = int(input('Digite a segunda nota do aluno: '))
    lista.append(nota_2)
    listas.append(lista[:])
    lista.clear()
    medias = (nota_1 + nota_2)/2
    media.append(str(medias))
    aluno = str(input('Digite o nome do aluno: (999 interrompe): '))
    numero += 1
print ('-='*30)
print ('No.',  'NOME'.ljust(5, ' '), 'MÉDIA'.rjust(17, ' '))
print ('-'*30)
x = 0
y = 1
for c in range (0, len(listas)):
    print(listas[c][0].ljust(3, ' '), media[x].ljust(8, ' '), media [y].rjust(13, ' '))
    x += 2
    y += 2
print ('-'*30)
while individual != '999':
    individual = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    print (f'As notas do aluno {listas[individual][1]} são {listas[individual][2]} e {listas[individual][3]}')
    print('-' * 30)
print('Operação finalizada')
