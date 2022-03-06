expressao = list(str(input('Digite uma expressão: ')).lower())
w = expressao.count('(')
z = expressao.count(')')
x = expressao.index('(')
y = expressao.index(')')
if w != z:
    print('A expressão está errada')
if x > y:
    print('A expressão está errada')
if w == z:
    while x < y:
        if '(' in expressao:
            x = expressao.index('(')
            y = expressao.index(')')
            expressao.pop(x)
            expressao.pop(y-1)
        if '(' in expressao:
            x = expressao.index('(')
            y = expressao.index(')')
            w = expressao.count('(')
            if w == 0:
                print('A expressão está certa')
                break
            if y < x:
                print('A expressão está errada')
                break
        else:
            print('A expressão está certa')
            break
