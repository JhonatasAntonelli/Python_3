#modularização é o ato de construir modulos, ou seja, dividir um programa grande em programas pequenos.
# Foi criado um aruivo .py com as funções utilizadas aqui
# quando foi importado o arquivo, também foi importado as funções
# vantagens:
#organização do código
#Facilidade de manutenção
#ocultação de código detalhado
#Reutilização em outros projetos
import Uteis
# from Uteis import fatorial, dobro, triplo também daria certo, mas assim pode dar conflito se tiver outra função de mesmo nome
num = int(input('Digite um valor: '))
fat = Uteis.fatorial(num)
print(f'Ofatorial de {num} é {fat}')
print(f'O dobro de {num} é {Uteis.dobro(num)}')
print(f'O triplo de {num} é {Uteis.triplo(num)}')
# pacote é um arquivo com varias modularizações, que podem ser separadpos por assuntos
#para importar é igual a modularização
#No python toda pasta é considerado um pacotes
#  A sitacs para pacotes é __init__.py
# Ao invez de criar um arquivo.py se cria um python Packege que pode ter outros pacotes dentro de pacotes
#organizando por assunto