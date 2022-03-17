from time import sleep
from Ex115.lib.interface import * #O * vai importar tudo da pasta
while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma Opção valida \033[m')
    sleep(2)