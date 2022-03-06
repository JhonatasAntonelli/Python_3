x = int(input('Digite a quantidade de linha que você quer na sua matriz: '))
y = int(input('Digite a quantidade de colunas que você quer na sua matriz: '))
coluna = list()
linha_coluna = list()
soma_par = 0
soma_3_coluna = 0
valor = 0
for a in range (0,x):
    for c in range (0,y):
        n_coluna = int(input(f'Digite o valor para linha {a+1} coluna {c+1}: '))
        if n_coluna % 2 == 0:
            soma_par = n_coluna + soma_par
        coluna.append(n_coluna)
        if c == 2:
            soma_3_coluna = n_coluna + soma_3_coluna
        if a == 1:
            if n_coluna > valor:
                valor = n_coluna
    linha = coluna [:]
    coluna.clear()
    linha_coluna.append(linha[:])
for b in range (0,x):
    print (f'{linha_coluna[b]}')
print(f'A soma de todos os números pares digitados é {soma_par}')
print (f'A soma de todos os números da terceira coluna é {soma_3_coluna}')
print (f'O maior valor da segunda linha é {valor}')