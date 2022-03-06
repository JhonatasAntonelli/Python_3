def fatoral(num, show = True):
    fatorado = 1
    for c in range (num, 0, -1):
        if show:
            print(f'{c}',end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        fatorado *= c
    return fatorado
num = int(input('Qual número você quer fatorar? '))
print (f'{fatoral(num, True)}')