print ('-'*60)
titulo = ' LISTAGEM DE PREÇOS '
print(titulo.center(60, '*'))
print ('-'*60)
lista = ('Lápis', 1.75, 'Caderno', 15.90, 'Borracha', 2.00, 'Estojo', 22.00, 'Transferidos', 4.2)
x = int(len(lista)/2)
y = 0
z = 1
for c in range (0,x):
    d = str(lista[z])
    print(lista[y].ljust(50, '.'),'R$', d.rjust(5, ' '))
    y += 2
    z += 2
print ('-'*60)