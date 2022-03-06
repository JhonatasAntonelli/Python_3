from datetime import datetime
def voto(num):
    anoatual = datetime.now().year
    idade = anoatual - num
    if idade >= 65:
        resposta = 'VOTO É OPCIONAL!'
    if idade >= 18 and idade < 65:
        resposta = 'VOTO É OBRIGATÓRIO!'
    if idade >= 16 and idade < 18:
        resposta = 'VOTO É OPCIONAL!'
    if idade < 16:
        resposta = 'VOTO É NEGADO!'
    return resposta, idade

num = int(input('Qual seu ano de nascimento? '))
voto(num)
resposta, idade = voto(num)
print (f'Com {idade} anos o {resposta}')