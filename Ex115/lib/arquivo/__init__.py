from Ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')#o mais serve para criar o arquivo, caso ele não exista
        a.close()
    except:
        print('Houve um erro na cração so arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt') #rt serve para ler o arquivo
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')#Isso faz com que os dados sejam separados por ;
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')#at serve para adicionar coissa ao arquivo
    except:
        print('Houve um Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')#a.write vai escrever no arquivo
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close