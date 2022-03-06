dados = dict()
alunos = list()
dados['nome'] = str(input('Qual o nome do aluno (999 interrompe)? '))
while dados ['nome'] != '999':
    media = float(input('Qual a média do aluno (999 interrompe)? '))
    if media >= 7:
        dados['situação'] = 'Aprovado'
    if media < 7:
        dados['situação'] = 'Reprovado'
    media = str(media)
    dados['media'] = media
    alunos.append(dados.copy())
    dados['nome'] = str(input('Qual o nome do aluno (999 interrompe)? '))
print(alunos[0]['nome'])
print ('-='*30)
print ('NOME'.ljust(10, ' '),  'MÉDIA'.ljust(13, ' '), 'SITUAÇÃO'.ljust(15, ' '))
print ('-'*40)
for c in range (0, len(alunos)):
    print(alunos[c]['nome'].ljust(10, ' '), alunos[c]['media'].ljust(13, ' '), alunos[c]['situação'].ljust(15, ' '))
print ('-'*40)
