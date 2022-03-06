x = int(input('Digite a quantidade de linha que você quer na sua matriz: '))
y = int(input('Digite a quantidade de colunas que você quer na sua matriz: '))
coluna = list()
linha_coluna = list()
for a in range (0,x):
    for c in range (0,y):
        n_coluna = int(input(f'Digite o valor para linha {a+1} coluna {c+1}: '))
        coluna.append(n_coluna)
    linha = coluna [:]
    coluna.clear()
    linha_coluna.append(linha[:])
for b in range (0,x):
    print (f'{linha_coluna[b]}')