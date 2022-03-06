# se digitar help() ele apresenta as funcionalidade de uma função
help(print) #isso mostra a docstring (manual) da funçaõ
"""O docstring é adicionado colocando o manual entre 3 aspas duplas, 
isso vai aparecer quando digitar help()"""
def somar (a=0,b=0,c=0):#se colocar o =0 caso o valor de c não seja adicionado, ele sera considerado 0.
    s = a+b+c
    return s#isso faz com que o valor seja retornado como variavel global

r1 = (somar(3,2,5))
r2 = somar(8,4)
r3 = somar(c=3, b=5)
print (f'As somas deram {r1}, {r2} e {r3}')
def teste(b):
    global a # se fizer isso o valor de 'a' global será o novo valor
    a = 8 #local e se não definir o 'global a' então sera criada uma variavel 'a' local
    #como o 'a' foi definido dentro da fução, dentro dessa função o 'a' valoe 8
    #caso o 'a' não seja definido dentro da função, sera utilizado o 'a' global
    b+=4
    c=2
    print (a, b, c)
a = 5 #global
teste(a)
print (a)#como está fora da função, será utilizado o 'a' global
