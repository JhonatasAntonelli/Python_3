from num2words import num2words
numero = input('Digite um número: ')
valido = 0
while valido == 0:
    if numero >= '0' and numero <= '20':
        valido +=1
    if numero.isalpha():
        numero = input('Digite um número: ')
    if numero < '0' or numero > '20':
        numero = input('Digite um número: ')
numero = int(numero)

print(num2words(numero, lang = 'pt_br', to = 'ordinal'))
print(num2words(numero, lang = 'pt_br', to = 'ordinal_num'))
print(num2words(numero, lang = 'pt_br', to = 'year'))
print(num2words(numero, lang = 'pt_br', to = 'currency'))
print(num2words(numero, lang ='es'))

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print (numeros[numero])