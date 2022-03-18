from time import sleep
from Ex115.lib.arquivo import *
from Ex115.lib.interface import * #O * vai importar tudo da pa

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opçao de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma Opção valida \033[m')
    sleep(2)