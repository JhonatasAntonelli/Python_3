'''palavra = 1
x = 0
while palavra != '0':
    palavra = str(input('\nDigite uma palavra: ')).lower()
    print(f'Na palavra {palavra} temos as vogais:', end=" ")
    if palavra == '0':
        break
    palavra = palavra.split()
    junto = ''.join(palavra)
    separado = ''
    for letra in range(0, len(junto), 1):
        letra = junto[letra]
        if 'a' == letra [x]:
            print ('a', end=" ")
        if 'e' == letra [x]:
            print ('e', end=" ")
        if 'i' == letra [x]:
            print ('i', end=" ")
        if 'o' == letra [x]:
            print ('o', end=" ")
        if 'u' == letra [x]:
            print('u', end=" ")'''
palavras = ('pastel', 'paralelepipedo', 'ventilador', 'cafe', 'computador')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print (letra, end=' ')

