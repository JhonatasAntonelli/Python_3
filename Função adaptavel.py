frase = '0'
while frase != '999':
    frase = str(input('Digite uma frase: (999 interrompe): '))
    x = (len(frase))
    def escreva (*frase):
        print ('-'*(x+4))
    escreva(*frase)
    print (f'  {frase}  ')
    escreva(*frase)