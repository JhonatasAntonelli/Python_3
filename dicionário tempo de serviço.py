from datetime import datetime
dados = dict()
nome = str(input('Qual o seu nome? '))
todos = list()
while nome != '999':
    nascimento = int(input('Qual a date de nascimento? '))
    idade = datetime.now().year - nascimento
    ctps = int(input('Qual o número da sua carteira de trabalho? (0 é não tem): '))
    dados['Nome'] = nome
    dados['Idade'] = idade
    dados['CTPS'] = ctps
    if ctps != 0:
        contratacao = int(input('Qual o ano de contratação? '))
        aposentadoria = contratacao - nascimento + 35
        salario = int(input('Qual o seu salário? '))
        dados ['Contratação'] = contratacao
        dados ['Salário'] = salario
        dados ['Aposentadoria'] = aposentadoria
    todos.append(dados.copy())
    nome = str(input('Qual o seu nome? (999 interrompe): '))
print (todos)
for e in todos:
    for c, v in e.items():
        print (f'{c} tem valor: {v} ')
